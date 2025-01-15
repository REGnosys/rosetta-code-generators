'''func proxy'''
import inspect
import functools

__all__ = ['FuncProxy', 'replaceable', 'create_module_attr_guardian']


class FuncProxy:
    '''A callable proxy allowing functions to be replaced at runtime'''
    __slots__ = ('_func',)

    def __init__(self, func):
        self._func = func

    def __call__(self, *args, **kwargs):
        '''pass the call to the current function'''
        return self._func(*args, **kwargs)

    @property
    def func(self):
        '''current function'''
        return self._func

    @func.setter
    def func(self, func):
        '''replace the current function with a new one'''
        self.__assign__(func)

    def __assign__(self, func):
        '''assigns the new function and checks parameter list compatibility'''
        if not callable(func):
            raise ValueError(f'Need a callable, but got {str(func)}')

        curr_params = inspect.signature(self._func).parameters
        new_params = inspect.signature(func).parameters
        if curr_params.keys() != new_params.keys():
            raise ValueError(
                'Replacement function parameter list do not match the current '
                f'parameter list of {str(self._func)}'
            )
        self._func = func


def replaceable(func):
    '''wrapper for a function which can be replaced at runtime'''
    proxy = FuncProxy(func)

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return proxy(*args, **kwargs)

    wrapper.__assign__ = proxy.__assign__  # type: ignore
    return wrapper


def create_module_attr_guardian(module):
    '''Returns a module setter class derived from the invoking module'''
    # pylint: disable=too-few-public-methods
    class ModuleAttrSetter(module):
        ''' Redirects the assignment of an attribute to its __assign__ method
            if defined, otherwise the default functionality is used and the
            attribute is just replaced.
        '''
        def __setattr__(self, attr, val):
            exists = getattr(self, attr, None)
            if exists is not None and hasattr(exists, '__assign__'):
                exists.__assign__(val)
            else:
                super().__setattr__(attr, val)
    return ModuleAttrSetter

# EOF
