'''Utility functions (runtime) for rosetta models.'''
from __future__ import annotations
import logging as log
import keyword
import inspect
from enum import Enum
from typing import get_args, get_origin
from typing import TypeVar, Generic, Callable, Any
from collections import defaultdict
from pydantic import BaseModel, ValidationError, ConfigDict

__all__ = [
    'if_cond', 'if_cond_fn', 'Multiprop', 'rosetta_condition', 'BaseDataClass',
    'ConditionViolationError', 'any_elements', 'get_only_element',
    'rosetta_filter', 'all_elements', 'contains', 'disjoint', 'join',
    'rosetta_local_condition', 'execute_local_conditions', 'flatten_list',
    'rosetta_resolve_attr', 'rosetta_resolve_deep_attr', 'rosetta_count',
    'rosetta_attr_exists', '_get_rosetta_object', 'set_rosetta_attr',
    'add_rosetta_attr', 'check_cardinality', 'AttributeWithMeta',
    'AttributeWithAddress', 'AttributeWithReference',
    'AttributeWithMetaWithAddress', 'AttributeWithMetaWithReference',
    'AttributeWithAddressWithReference',
    'AttributeWithMetaWithAddressWithReference', 'rosetta_str',
    'rosetta_check_one_of'
]


def if_cond(ifexpr, thenexpr: str, elseexpr: str, obj: object):
    '''A helper to return the value of the ternary operator.'''
    expr = thenexpr if ifexpr else elseexpr
    return eval(expr, globals(), {'self': obj})  # pylint: disable=eval-used


def if_cond_fn(ifexpr, thenexpr: Callable, elseexpr: Callable) -> Any:
    ''' A helper to return the value of the ternary operator
        (functional version).
    '''
    expr = thenexpr if ifexpr else elseexpr
    return expr()


def _to_list(obj) -> list | tuple:
    if isinstance(obj, (list, tuple)):
        return obj
    return (obj, )


def _is_meta(obj: Any) -> bool:
    '''Returns true if it is a meta data with embedded rosetta type.'''
    return isinstance(
        obj, (AttributeWithMeta, AttributeWithAddress,
              AttributeWithMetaWithAddress, AttributeWithMetaWithReference,
              AttributeWithMetaWithAddressWithReference))


def mangle_name(attrib: str) -> str:
    ''' Mangle any attrib that is a Python keyword, is a Python soft keyword
        or begins with _
    '''
    if (keyword.iskeyword(attrib) or keyword.issoftkeyword(attrib)
            or attrib.startswith('_')):
        return 'rosetta_attr_' + attrib
    return attrib


def rosetta_resolve_attr(obj: Any | None,
                         attrib: str) -> Any | list[Any] | None:
    ''' Rosetta semantics compliant attribute resolver.
        Lists and mangled attributes are treated as defined by
        the rosetta definition (list flattening).
    '''
    if obj is None:
        return None
    if isinstance(obj, (list, tuple)):
        res = [
            item for elem in obj
            for item in _to_list(rosetta_resolve_attr(elem, attrib))
            if item is not None
        ]
        return res if res else None
    if _is_meta(obj):
        # NOTE: ignores (for now) all meta attributes in the expressions.
        # In the future one might want to check if the attrib is contained
        # in the metadata and return it instead of failing.
        obj = obj.value
    elif inspect.isframe(obj):
        obj = getattr(obj, 'f_locals')
    attrib = mangle_name(attrib)
    if isinstance(obj, dict):
        return obj[attrib]
    return getattr(obj, attrib, None)


def rosetta_resolve_deep_attr(obj: Any | None,
                              attrib: str) -> Any | list[Any] | None:
    ''' Resolves a "deep path" attribute. If the attribute or the object is
        not a "deep path" one, the function falls back to the regular
        `rosetta_resolve_attr`.
    '''
    # pylint: disable=protected-access
    if obj is None:
        return None
    # if not a "deep path" object or attribute, fall back to the std function
    if (not hasattr(obj, '_CHOICE_ALIAS_MAP')
            or attrib not in obj._CHOICE_ALIAS_MAP):
        return rosetta_resolve_attr(obj, attrib)

    for container_nm, getter_fn in obj._CHOICE_ALIAS_MAP[attrib]:
        if container_obj := rosetta_resolve_attr(obj, container_nm):
            return getter_fn(container_obj, attrib)
    return None


def rosetta_count(obj: Any | None) -> int:
    '''Implements the lose count semantics of the rosetta DSL'''
    if not obj:
        return 0
    try:
        return len(obj)
    except TypeError:
        return 1


def rosetta_attr_exists(val: Any) -> bool:
    '''Implements the Rosetta semantics of property existence'''
    if val is None or val == []:
        return False
    return True


def rosetta_str(x: Any) -> str:
    '''Returns a Rosetta conform string representation'''
    if isinstance(x, Enum):
        x = x.value
    return str(x)


def rosetta_check_one_of(obj, *attr_names, necessity=True) -> bool:
    """ Checks that one and only one attribute is set. """
    if inspect.isframe(obj):
        values = getattr(obj, 'f_locals')
    else:
        values = obj.model_dump()
    vals = [values.get(n) for n in attr_names]
    n_attr = sum(1 for v in vals if v is not None and v != [])
    if necessity and n_attr != 1:
        log.error('One and only one of %s should be set!', attr_names)
        return False
    if not necessity and n_attr > 1:
        log.error('Only one of %s can be set!', attr_names)
        return False
    return True


def _get_rosetta_object(base_model: str, attribute: str, value: Any) -> Any:
    model_class = globals()[base_model]
    instance_kwargs = {attribute: value}
    instance = model_class(**instance_kwargs)
    return instance


class Multiprop(list):
    ''' A class allowing for dot access to a attribute of all elements of a
        list.
    '''

    def __getattr__(self, attr):
        # return multiprop(getattr(x, attr) for x in self)
        res = Multiprop()
        for x in self:
            if isinstance(x, Multiprop):
                res.extend(x.__getattr__(attr))
            else:
                res.append(getattr(x, attr))
        return res


_CONDITIONS_REGISTRY: defaultdict[str, dict[str, Any]] = defaultdict(dict)


def rosetta_condition(condition):
    '''Wrapper to register all constraint functions in the global registry'''
    path_components = condition.__qualname__.split('.')
    path = '.'.join([condition.__module__ or ''] + path_components[:-1])
    name = path_components[-1]
    _CONDITIONS_REGISTRY[path][name] = condition

    return condition


def rosetta_local_condition(registry: dict):
    '''Registers a condition function in a local registry.'''

    def decorator(condition):
        path_components = condition.__qualname__.split('.')
        path = '.'.join([condition.__module__ or ''] + path_components)
        registry[path] = condition

        return condition

    return decorator


def execute_local_conditions(registry: dict, cond_type: str):
    '''Executes all registered in a local registry.'''
    for condition_path, condition_func in registry.items():
        if not condition_func():
            raise ConditionViolationError(
                f"{cond_type} '{condition_path}' failed.")


class ConditionViolationError(ValueError):
    '''Exception thrown on violation of a constraint'''


def _fqcn(cls) -> str:
    return '.'.join([cls.__module__ or '', cls.__qualname__])


def _get_conditions(cls) -> list:
    res = []
    index = cls.__mro__.index(BaseDataClass)
    for c in reversed(cls.__mro__[:index]):
        fqcn = _fqcn(c)
        res += [('.'.join([fqcn, k]), v)
                for k, v in _CONDITIONS_REGISTRY.get(fqcn, {}).items()]
    return res


class MetaAddress(BaseModel):  # pylint: disable=missing-class-docstring
    scope: str | None = None
    value: str


class BaseDataClass(BaseModel):
    ''' A base class for all cdm generated classes. It is derived from
        `pydantic.BaseModel` which provides type checking at object creation
        for all cdm classes. It provides as well the `validate_model`,
        `validate_conditions` and `validate_attribs` methods which perform the
        conditions, cardinality and type checks as specified in the rosetta
        type model. The method `validate_model` is not invoked automatically,
        but is left to the user to determine when to check the validity of the
        cdm model.
    '''
    model_config = ConfigDict(extra='forbid', revalidate_instances='always')

    meta: dict | None = None
    address: MetaAddress | None = None

    def validate_model(self,
                       recursively: bool = True,
                       raise_exc: bool = True,
                       strict: bool = True) -> list:
        ''' This method performs full model validation. It will validate all
            attributes and it will also invoke `validate_conditions` to check
            all conditions and the cardinality of all attributes of this object.
            The parameter `raise_exc` controls whether an exception should be
            thrown if a validation or condition is violated or if a list with
            all encountered violations should be returned instead.
        '''
        att_errors = self.validate_attribs(raise_exc=raise_exc, strict=strict)
        return att_errors + self.validate_conditions(recursively=recursively,
                                                     raise_exc=raise_exc)

    def validate_attribs(self,
                         raise_exc: bool = True,
                         strict: bool = True) -> list:
        ''' This method performs attribute type validation.
            The parameter `raise_exc` controls whether an exception should be
            thrown if a validation or condition is violated or if a list with
            all encountered violations should be returned instead.
        '''
        try:
            self.model_validate(self, strict=strict)
        except ValidationError as validation_error:
            if raise_exc and validation_error:
                raise validation_error
            return [validation_error]
        return []

    def validate_conditions(self,
                            recursively: bool = True,
                            raise_exc: bool = True) -> list:
        ''' This method will check all conditions and the cardinality of all
            attributes of this object. This includes conditions and cardinality
            of properties specified in the base classes. If the parameter
            `recursively` is set to `True`, it will invoke the validation on the
            rosetta defined attributes of this object too.
            The parameter `raise_exc` controls whether an exception should be
            thrown if a condition is not met or if a list with all encountered
            condition violations should be returned instead.
        '''
        self_rep = object.__repr__(self)
        log.info('Checking conditions for %s ...', self_rep)
        exceptions = []
        for name, condition in _get_conditions(self.__class__):
            log.info('Checking condition %s for %s...', name, self_rep)
            if not condition(self):
                msg = f'Condition "{name}" for {repr(self)} failed!'
                log.error(msg)
                exc = ConditionViolationError(msg)
                if raise_exc:
                    raise exc
                exceptions.append(exc)
            else:
                log.info('Condition %s for %s satisfied.', name, self_rep)
        if recursively:
            for k, v in self.__dict__.items():
                log.info('Validating conditions of property %s', k)
                exceptions += _validate_conditions_recursively(
                    v, raise_exc=raise_exc)
        err = f'with {len(exceptions)}' if exceptions else 'without'
        log.info('Done conditions checking for %s %s errors.', self_rep, err)
        return exceptions

    def add_to_list_attribute(self, attr_name: str, value) -> None:
        """
        Adds a value to a list attribute, ensuring the value is of an allowed
        type.

        Parameters:
        attr_name (str): Name of the list attribute.
        value: Value to add to the list.

        Raises:
        AttributeError: If the attribute name is not found or not a list.
        TypeError: If the value type is not one of the allowed types.
        """
        if not hasattr(self, attr_name):
            raise AttributeError(f"Attribute {attr_name} not found.")

        attr = getattr(self, attr_name)
        if not isinstance(attr, list):
            raise AttributeError(f"Attribute {attr_name} is not a list.")

        # Get allowed types for the list elements
        allowed_types = get_allowed_types_for_list_field(
            self.__class__, attr_name)

        # Check if value is an instance of one of the allowed types
        if not isinstance(value, allowed_types):
            raise TypeError(f"Value must be an instance of {allowed_types}, "
                            f"not {type(value)}")

        attr.append(value)


def _validate_conditions_recursively(obj, raise_exc=True):
    '''Helper to execute conditions recursively on a model.'''
    if not obj:
        return []
    if isinstance(obj, BaseDataClass):
        return obj.validate_conditions(
            recursively=True,  # type:ignore
            raise_exc=raise_exc)
    if isinstance(obj, (list, tuple)):
        exc = []
        for item in obj:
            exc += _validate_conditions_recursively(item, raise_exc=raise_exc)
        return exc
    if _is_meta(obj):
        return _validate_conditions_recursively(obj.value, raise_exc=raise_exc)
    return []


def get_allowed_types_for_list_field(model_class: type, field_name: str):
    """
    Gets the allowed types for a list field in a Pydantic model, supporting
    both Union and | operator.

    Parameters:
    model_class (type): The Pydantic model class.
    field_name (str): The field name.

    Returns:
    tuple: A tuple of allowed types.
    """
    field_type = model_class.__annotations__.get(field_name)
    if field_type and get_origin(field_type) is list:
        list_elem_type = get_args(field_type)[0]
        if get_origin(list_elem_type):
            return get_args(list_elem_type)
        return (list_elem_type, )  # Single type or | operator used
    return ()


ValueT = TypeVar('ValueT')


class AttributeWithMeta(BaseModel, Generic[ValueT]):
    '''Meta support'''
    meta: dict | None = None
    value: ValueT


class AttributeWithAddress(BaseModel, Generic[ValueT]):
    '''Meta support'''
    address: MetaAddress | None = None
    value: ValueT | None = None


class AttributeWithReference(BaseDataClass):
    '''Meta support'''
    externalReference: str | None = None
    globalReference: str | None = None


class AttributeWithMetaWithAddress(BaseModel, Generic[ValueT]):
    '''Meta support'''
    meta: dict | None = None
    address: MetaAddress | None = None
    value: ValueT


class AttributeWithMetaWithReference(BaseModel, Generic[ValueT]):
    '''Meta support'''
    meta: dict | None = None
    externalReference: str | None = None
    globalReference: str | None = None
    value: ValueT


class AttributeWithAddressWithReference(BaseModel, Generic[ValueT]):
    '''Meta support'''
    address: MetaAddress | None = None
    externalReference: str | None = None
    globalReference: str | None = None
    value: ValueT


class AttributeWithMetaWithAddressWithReference(BaseModel, Generic[ValueT]):
    '''Meta support'''
    meta: dict | None = None
    address: MetaAddress | None = None
    externalReference: str | None = None
    globalReference: str | None = None
    value: ValueT


def _ntoz(v):
    '''Support the lose rosetta treatment of None in comparisons'''
    if v is None:
        return 0
    return v


_cmp = {
    '=': lambda x, y: _ntoz(x) == _ntoz(y),
    '<>': lambda x, y: _ntoz(x) != _ntoz(y),
    '>=': lambda x, y: _ntoz(x) >= _ntoz(y),
    '<=': lambda x, y: _ntoz(x) <= _ntoz(y),
    '>': lambda x, y: _ntoz(x) > _ntoz(y),
    '<': lambda x, y: _ntoz(x) < _ntoz(y)
}


def all_elements(lhs, op, rhs) -> bool:
    '''Checks that two lists have the same elements'''
    cmp = _cmp[op]
    op1 = _to_list(lhs)
    op2 = _to_list(rhs)

    return all(cmp(el1, el2) for el1, el2 in zip(op1, op2)) if len(op1) == len(op2) else False

def disjoint(op1, op2):
    '''Checks if two lists have no common elements'''
    op1 = set(_to_list(op1))
    op2 = set(_to_list(op2))
    return not op1 & op2


def contains(op1, op2):
    ''' Checks if op2 is contained in op1
        (e.g. every element of op2 is in op1)
    '''
    op1 = set(_to_list(op1))
    op2 = set(_to_list(op2))

    return op2.issubset(op1)


def join(lst, sep=''):
    ''' Joins the string representation of the list elements, optionally
        separated.
    '''
    return sep.join([str(el) for el in lst])


def any_elements(lhs, op, rhs) -> bool:
    '''Checks if to lists have any common element(s)'''
    cmp = _cmp[op]
    op1 = _to_list(lhs)
    op2 = _to_list(rhs)

    return any(cmp(el1, el2) for el1 in op1 for el2 in op2)


def check_cardinality(prop, inf: int, sup: int | None = None) -> bool:
    ''' If the supremum is not supplied (e.g. is None), the property is
        unbounded (e.g. it corresponds to (x..*) in rosetta).
    '''
    if not prop:
        prop_card = 0
    elif isinstance(prop, (list, tuple)):
        prop_card = len(prop)
    else:
        prop_card = 1

    if sup is None:
        sup = prop_card

    return inf <= prop_card <= sup


def get_only_element(collection):
    ''' Returns the single element of a collection, if the list contains more
        more than one element or is empty, None is returned.
    '''
    if isinstance(collection, (list, tuple)) and len(collection) == 1:
        return collection[0]
    return None


def flatten_list(nested_list):
    '''flattens the list of lists (no-recursively)'''
    return [item for sublist in _to_list(nested_list) for item in _to_list(sublist)]


def rosetta_filter(items, filter_func):
    """
    Filters a list of items based on a specified filtering criteria provided as
    a boolean lambda function.

    :param items: List of items to be filtered.
    :param filter_func: A lambda function representing the boolean expression
        for filtering.
    :param item_name: The name used to refer to each item in the boolean
        expression.
    :return: Filtered list.
    """
    return [item for item in (items or []) if filter_func(item)]


def set_rosetta_attr(obj: Any, path: str, value: Any) -> None:
    """
    Sets an attribute of a Rosetta model object to a specified value using a
    path.

    Parameters:
    obj (Any): The object whose attribute is to be set.
    path (str): The path to the attribute, with components separated by '->'.
    value (Any): The value to set the attribute to.

    Raises:
    ValueError: If the object or attribute at any level in the path is None.
    AttributeError: If an invalid attribute path is provided.
    """
    if obj is None:
        raise ValueError(
            "Cannot set attribute on a None object in set_rosetta_attr.")

    path_components = path.split('->')  # Use '->' for splitting the path
    parent_obj = obj

    # Iterate through the path components, except the last one
    for attrib in path_components[:-1]:
        parent_obj = rosetta_resolve_attr(parent_obj, attrib)
        if parent_obj is None:
            raise ValueError(
                f"Attribute '{attrib}' in the path is None, cannot "
                "proceed to set value.")

    # Set the value to the last attribute in the path
    final_attr = path_components[-1]
    if hasattr(parent_obj, final_attr):
        setattr(parent_obj, final_attr, value)
    else:
        raise AttributeError(f"Invalid attribute '{final_attr}' for object of "
                             f"type {type(parent_obj).__name__}")


def add_rosetta_attr(obj: Any, attrib: str, value: Any) -> None:
    """
    Adds a value to a list-like attribute of a Rosetta model object.

    Parameters:
    obj (Any): The object whose attribute is to be modified.
    attrib (str): The list-like attribute to add the value to.
    value (Any): The value to add to the attribute.
    """
    if obj is not None:
        if hasattr(obj, attrib):
            current_attr = getattr(obj, attrib)
            if isinstance(current_attr, list):
                current_attr.append(value)
            else:
                raise TypeError(f"Attribute {attrib} is not list-like.")
        else:
            setattr(obj, attrib, [value])
    else:
        raise ValueError("Object for add_rosetta_attr cannot be None.")

# EOF
