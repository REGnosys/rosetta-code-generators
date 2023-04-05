import logging as log
from typing import Tuple
from functools import wraps
from collections import defaultdict
from pydantic import BaseModel

__all__ = ['if_cond', 'multiprop', 'cdm_condition', 'BaseDataClass',
           'ConditionViolationError', 'any_elements', 'all_elements',
           'check_cardinality']


def if_cond(ifexpr, thenexpr: str, elseexpr: str, obj: object):
    """ A helper to return the value of the ternary operator. """
    expr = thenexpr if ifexpr else elseexpr
    return eval(expr, globals(), {'self': obj})


class multiprop(list):
    def __getattr__(self, attr):
        # return multiprop(getattr(x, attr) for x in self)
        res = multiprop()
        for x in self:
            if isinstance(x, multiprop):
                res.extend(x.__getattr__(attr))
            else:
                res.append(getattr(x, attr))
        return res


_CONDITIONS_REGISTRY = defaultdict(dict)


def cdm_condition(condition):
    path_components = condition.__qualname__.split('.')
    path = '.'.join(path_components[:-1])
    name = path_components[-1]
    _CONDITIONS_REGISTRY[path][name] = condition

    @wraps(condition)
    def wrapper(*args, **kwargs):
        return condition(*args, **kwargs)
    return wrapper


class ConditionViolationError(ValueError):
    pass


class BaseDataClass(BaseModel):
    def validate_conditions(
        self, recursively: bool=True, raise_exc: bool=True
    ) -> Tuple[bool, list]:
        log.info('Checking conditions for %s ...', self)
        conditions = _CONDITIONS_REGISTRY.get(self.__class__.__qualname__, {})
        exceptions = []
        for name, condition in conditions.items():
            log.info('Checking condition %s.%s for %s...', 
                     self.__class__.__qualname__, name, self)
            if not condition(self):
                msg = (f'Condition "{self.__class__.__qualname__}.{name}" '
                       f'for {repr(self)} failed!')
                log.error(msg)
                exc = ConditionViolationError(msg)
                if raise_exc:
                    raise exc
                exceptions.append(exc)
            else:
                log.info(
                    'Condition %s.%s for %s statisfied.',
                     self.__class__.__qualname__, name, self
                )
        if recursively:
            for k, v in self.__dict__.items():
                if isinstance(v, BaseDataClass):
                    log.info(
                        'Invoking conditions validation on the property '
                        '"%s" of %s', k, self
                    )
                    _, exc = v.validate_conditions(
                        recursively=True, raise_exc=raise_exc
                    )
                    exceptions += exc
                    if exc:
                        log.error(
                            'Validation of the property "%s" of %s failed!',
                            k, self
                        )
        err = 'with' if exceptions else 'without'
        log.info('Done conditions checking for %s %s errors.', self, err)
        return not exceptions, exceptions

    def check_one_of_constraint(self, *attr_names, necessity=True) -> bool:
        """ Checks that one and only one attribute is set. """
        values = self.dict()
        vals = [values.get(n) for n in attr_names]
        n_attr = sum(1 for v in vals if v is not None)
        if necessity and n_attr != 1:
            log.error(f'One and only one of {attr_names} should be set!')
            return False
        if not necessity and n_attr > 1:
            log.error(f'Only one of {attr_names} can be set!')
            return False
        return True


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
    cmp = _cmp[op]
    op1 = _to_list(lhs)
    op2 = _to_list(rhs)

    return all(cmp(el1, el2) for el1 in op1 for el2 in op2)


def any_elements(lhs, op, rhs) -> bool:
    cmp = _cmp[op]
    op1 = _to_list(lhs)
    op2 = _to_list(rhs)

    return any(cmp(el1, el2) for el1 in op1 for el2 in op2)


def check_cardinality(prop, inf:int, sup:int = None) -> bool:
    """ If the supremum is not suppleid (e.g. is None), the property is
        unbounded (e.g. it corresponds to (x..*) in rosetta).
    """
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
