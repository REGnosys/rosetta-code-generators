# pylint: disable=missing-function-docstring
from rosetta.runtime.utils import rosetta_resolve_attr
from rosetta_dsl.test.semantic.PythonNameMangling import PythonNameMangling


def test_python_global_create():
    PythonNameMangling(rosetta_attr_global=5)


def test_python_global_create_validate():
    obj = PythonNameMangling(rosetta_attr_global=5)
    assert not obj.validate_model(raise_exc=False)


def test_python_global_rosetta_resolve_attr():
    obj = PythonNameMangling(rosetta_attr_global=5)
    val = rosetta_resolve_attr(obj, 'global')
    assert val == 5


if __name__ == '__main__':
    test_python_global_create()
    test_python_global_create_validate()
    test_python_global_rosetta_resolve_attr()

# EOF
