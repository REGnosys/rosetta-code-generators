'''Utility functions (runtime) for rosetta models.'''
from __future__ import annotations
import logging as log
from typing import TypeVar, Generic, Callable, Any
from functools import wraps
from collections import defaultdict
from pydantic.main import BaseModel, validate_model
from pydantic.generics import GenericModel
from pydantic import Extra



__all__ = ['if_cond', 'if_cond_fn', 'Multiprop', 'rosetta_condition',
           'BaseDataClass', 'ConditionViolationError', 'any_elements',
           'all_elements', 'contains', 'disjoint', 'join',
           'check_cardinality',
           'AttributeWithMeta',
           'AttributeWithAddress',
           'AttributeWithReference',
           'AttributeWithMetaWithAddress',
           'AttributeWithMetaWithReference',
           'AttributeWithAddressWithReference',
           'AttributeWithMetaWithAddressWithReference']


def if_cond(ifexpr, thenexpr: str, elseexpr: str, obj: object):
    '''A helper to return the value of the ternary operator.'''
    expr = thenexpr if ifexpr else elseexpr
    return eval(expr, globals(), {'self': obj})


def if_cond_fn(ifexpr, thenexpr: Callable, elseexpr: Callable) -> Any:
    '''A helper to return the value of the ternary operator (functional version).'''
    expr = thenexpr if ifexpr else elseexpr
    return expr()


class Multiprop(list):
    '''A class allowing for dot access to a attribute of all elements of a list'''
    def __getattr__(self, attr):
        # return multiprop(getattr(x, attr) for x in self)
        res = Multiprop()
        for x in self:
            if isinstance(x, Multiprop):
                res.extend(x.__getattr__(attr))
            else:
                res.append(getattr(x, attr))
        return res


_CONDITIONS_REGISTRY = defaultdict(dict)


def rosetta_condition(condition):
    '''Wrapper to register all constraint functions in the global registry'''
    path_components = condition.__qualname__.split('.')
    path = '.'.join([condition.__module__ or ''] + path_components[:-1])
    name = path_components[-1]
    _CONDITIONS_REGISTRY[path][name] = condition

    @wraps(condition)
    def wrapper(*args, **kwargs):
        return condition(*args, **kwargs)
    return wrapper


class ConditionViolationError(ValueError):
    '''Exception thrown on violation of a constraint'''
    pass


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
    scope: str
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

    meta: dict | None = None
    address: MetaAddress | None = None

    class Config:
        '''Disables the validity of extra parameters'''
        extra = Extra.forbid

    def validate_model(self,
                       recursively: bool = True,
                       raise_exc: bool = True) -> list:
        ''' This method performs full model validation. It will validate all
            attributes and it will also invoke `validate_conditions` to check
            all conditions and the cardinality of all attributes of this object.
            The parameter `raise_exc` controls whether an exception should be
            thrown if a validation or condition is violated or if a list with
            all encountered violations should be returned instead.
        '''
        att_errors = self.validate_attribs(raise_exc=raise_exc)
        return att_errors + self.validate_conditions(recursively=recursively,
                                                     raise_exc=raise_exc)

    def validate_attribs(self, raise_exc: bool = True) -> list:
        ''' This method performs attribute type validation.
            The parameter `raise_exc` controls whether an exception should be
            thrown if a validation or condition is violated or if a list with
            all encountered violations should be returned instead.
        '''
        *_, validation_error = validate_model(self.__class__, self.__dict__)
        if raise_exc and validation_error:
            raise validation_error
        return [validation_error] if validation_error else []

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
        log.info('Checking conditions for %s ...', self)
        exceptions = []
        for name, condition in _get_conditions(self.__class__):
            log.info('Checking condition %s for %s...', name, self)
            if not condition(self):
                msg = f'Condition "{name}" for {repr(self)} failed!'
                log.error(msg)
                exc = ConditionViolationError(msg)
                if raise_exc:
                    raise exc
                exceptions.append(exc)
            else:
                log.info('Condition %s for %s satisfied.', name, self)
        if recursively:
            for k, v in self.__dict__.items():
                if isinstance(v, BaseDataClass):
                    log.info(
                        'Invoking conditions validation on the property '
                        '"%s" of %s', k, self
                    )
                    exc = v.validate_conditions(recursively=True,
                                                raise_exc=raise_exc)
                    exceptions += exc
                    if exc:
                        log.error(
                            'Validation of the property "%s" of %s failed!', k,
                            self)
        err = 'with' if exceptions else 'without'
        log.info('Done conditions checking for %s %s errors.', self, err)
        return exceptions

    def check_one_of_constraint(self, *attr_names, necessity=True) -> bool:
        """ Checks that one and only one attribute is set. """
        values = self.dict()
        vals = [values.get(n) for n in attr_names]
        n_attr = sum(1 for v in vals if v is not None)
        if necessity and n_attr != 1:
            log.error('One and only one of %s should be set!', attr_names)
            return False
        if not necessity and n_attr > 1:
            log.error('Only one of %s can be set!', attr_names)
            return False
        return True


ValueT = TypeVar('ValueT')


class AttributeWithMeta(GenericModel, Generic[ValueT]):  # pylint: disable=missing-class-docstring
    meta: dict | None = None
    value: ValueT


class AttributeWithAddress(GenericModel, Generic[ValueT]):  # pylint: disable=missing-class-docstring
    address: MetaAddress | None = None
    value: ValueT | None = None


class AttributeWithReference(BaseDataClass):  # pylint: disable=missing-class-docstring
    externalReference: str | None = None
    globalReference: str | None = None


class AttributeWithMetaWithAddress(GenericModel, Generic[ValueT]):  # pylint: disable=missing-class-docstring
    meta: dict | None = None
    address: MetaAddress | None = None
    value: ValueT


class AttributeWithMetaWithReference(GenericModel, Generic[ValueT]):  # pylint: disable=missing-class-docstring
    meta: dict | None = None
    externalReference: str | None = None
    globalReference: str | None = None
    value: ValueT


class AttributeWithAddressWithReference(GenericModel, Generic[ValueT]):  # pylint: disable=missing-class-docstring
    address: MetaAddress | None = None
    externalReference: str | None = None
    globalReference: str | None = None
    value: ValueT


class AttributeWithMetaWithAddressWithReference(GenericModel, Generic[ValueT]):  # pylint: disable=missing-class-docstring
    meta: dict | None = None
    address: MetaAddress | None = None
    externalReference: str | None = None
    globalReference: str | None = None
    value: ValueT


_cmp = {
    '=': lambda x, y: x == y,
    '<>': lambda x, y: x != y,
    '>=': lambda x, y: x >= y,
    '<=': lambda x, y: x <= y,
    '>': lambda x, y: x > y,
    '<': lambda x, y: x < y
}


def _to_list(op) -> list|tuple:
    if isinstance(op, (list, tuple)):
        return op
    return (op,)


def all_elements(lhs, op, rhs) -> bool:
    '''Checks that two lists have the same elements'''
    cmp = _cmp[op]
    op1 = _to_list(lhs)
    op2 = _to_list(rhs)

    return all(cmp(el1, el2) for el1 in op1 for el2 in op2)


def disjoint(op1, op2):
    '''Checks if two lists have no common elements'''
    op1 = set(_to_list(op1))
    op2 = set(_to_list(op2))
    return not op1 & op2


def contains(op1, op2):
    '''Checks if op2 is contained in op1 (e.g. every element of op2 is in op1)'''
    op1 = set(_to_list(op1))
    op2 = set(_to_list(op2))

    return op2.issubset(op1)


def join(lst, sep=''):
    '''Joins the string representation of the list elements, optionally separted'''
    return sep.join([str(el) for el in lst])


def any_elements(lhs, op, rhs) -> bool:
    '''Checks if to lists have any comon element(s)'''
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

# EOF
