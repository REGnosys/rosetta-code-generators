import pytest
from rosetta.runtime.utils import rosetta_resolve_attr
from rosetta_dsl.test.model.ClassMemberAccess import ClassMemberAccess
 
class_member_access = ClassMemberAccess(one=42, three=[1, 2, 3])

def test_attribute_single ():
    assert rosetta_resolve_attr(class_member_access, 'one') == 42
def test_attribute_optional ():
    assert rosetta_resolve_attr(class_member_access, 'two') is None
def test_attribute_multi ():
    assert rosetta_resolve_attr(class_member_access, 'three') == [1, 2, 3]
def test_attribute_single_collection (): 
    assert rosetta_resolve_attr([class_member_access, class_member_access], 'one') == [42, 42]
def test_attribute_optional_collection (): 
    assert rosetta_resolve_attr([class_member_access, class_member_access], 'two') is None
def test_attribute_multi_collection ():
    assert rosetta_resolve_attr([class_member_access, class_member_access], 'three') == [1, 2, 3, 1, 2, 3]

if __name__ == "__main__":
    test_attribute_single ()
    test_attribute_optional ()
    test_attribute_multi ()
    test_attribute_single_collection () 
    test_attribute_optional_collection () 
    test_attribute_multi_collection ()