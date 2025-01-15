'''deep path unit tests'''
import pytest

from rosetta_dsl.test.semantic.deep_path.Deep1 import Deep1
from rosetta_dsl.test.semantic.deep_path.Bar1 import Bar1
from rosetta_dsl.test.semantic.deep_path.Bar2 import Bar2
from rosetta_dsl.test.semantic.deep_path.Bar3 import Bar3
from rosetta_dsl.test.semantic.deep_path.Bar4 import Bar4
from rosetta_dsl.test.semantic.deep_path.Foo import Foo

def create_foo_from_bar1 (attr: int):
    deep1 = Deep1(attr = attr)
    bar1 = Bar1(deep1 = deep1, b1 = 10, a = 10)
    return Foo(bar1 = bar1)

def create_foo_from_bar3_with_bar2 (attr: int):
    deep1 = Deep1(attr = attr)
    bar2 = Bar2(deep1 = deep1, b1 = 10, c = 10)
    bar3 = Bar3(bar2 = bar2)
    return Foo(bar3 = bar3)

def create_foo_from_bar3_with_bar4 (attr: int):
    deep1 = Deep1(attr = attr)
    bar4 = Bar4(deep1 = deep1, b1 = 10)
    bar3 = Bar3(bar4 = bar4)
    return Foo(bar3 = bar3)

def test_deep_path_bar1():
    foo = create_foo_from_bar1(attr=2)
    with pytest.raises(Exception):
        foo.validate_model()
    foo = create_foo_from_bar1(attr=3)
    assert len(foo.validate_model()) == 0

def test_deep_path_bar3_with_bar2():
    foo = create_foo_from_bar3_with_bar2(attr=2)
    with pytest.raises(Exception):
        foo.validate_model()
    foo = create_foo_from_bar3_with_bar2(attr=3)
    assert len(foo.validate_model()) == 0

def test_deep_path_bar3_with_bar4():
    foo = create_foo_from_bar3_with_bar4(attr=2)
    with pytest.raises(Exception):
        foo.validate_model()
    foo = create_foo_from_bar3_with_bar4(attr=3)
    assert len(foo.validate_model()) == 0

if __name__ == "__main__":
    test_deep_path_bar1()
    test_deep_path_bar3_with_bar2()
    test_deep_path_bar3_with_bar4()
