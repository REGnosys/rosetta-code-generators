
from cdm.utils import Multiprop
from cdm.utils import check_cardinality, join, contains, disjoint
# pylint: disable=missing-function-docstring, invalid-name, missing-class-docstring, too-few-public-methods


class A:
    def __init__(self, a):
        self.a = a
        self.b = a**2


class C:
    def __init__(self):
        self.c = Multiprop([A(2), A(3)])


class B:
    def __init__(self, i):
        self.b = Multiprop(C() for i in range(0, i))


class A0:
    def __init__(self, a):
        self.a0 = a


class A1:
    def __init__(self, x):
        self.a1 = Multiprop((A0(i) for i in range(0, x)))


class B1:
    def __init__(self, i):
        self.b1 = A1(i)


class C1:
    def __init__(self):
        self.c1 = Multiprop([B1(3), B1(0), B1(5)])


class C0:
    def __init__(self):
        self.c0 = C1()


def test_multiprop():
    x = Multiprop(range(0, 10))
    assert x == list(range(0, 10))

    y = Multiprop(A(i) for i in range(0, 10))
    assert y.a == list(range(0, 10))
    assert y.b == [i**2 for i in range(0, 10)]

    z = Multiprop(B(i) for i in range(1, 10))
    assert z.b.c.b == [4, 9] * 45


def test_multiprop_int():
    c = C0()
    assert c.c0.c1.b1.a1.a0 == [0, 1, 2, 0, 1, 2, 3, 4]
    assert 3 in c.c0.c1.b1.a1.a0


class T:
    def __init__(self, x):
        self.x = x


def test_check_cardinality_1_1():
    self = T(1)
    assert check_cardinality(self.x, 1, 1)
    assert check_cardinality(self.x, 1, 2)
    assert check_cardinality(self.x, 1, None)
    assert not check_cardinality(self.x, 2, 3)


def test_check_cardinality_0_1():
    self = T(None)
    assert check_cardinality(self.x, 0, 1)
    assert check_cardinality(self.x, 0, 2)
    assert check_cardinality(self.x, 0, None)
    assert not check_cardinality(self.x, 1, 1)
    assert not check_cardinality(self.x, 1, 2)
    assert not check_cardinality(self.x, 1, None)

    self = T(1)
    assert check_cardinality(self.x, 0, 1)
    assert check_cardinality(self.x, 0, 2)
    assert check_cardinality(self.x, 0, None)
    assert check_cardinality(self.x, 1, 1)
    assert check_cardinality(self.x, 1, 2)
    assert check_cardinality(self.x, 1, None)
    assert not check_cardinality(self.x, 2, 3)


def test_check_cardinality_list():
    self = T([1, 2, 3])
    assert check_cardinality(self.x, 0, None)
    assert check_cardinality(self.x, 0, 3)
    assert check_cardinality(self.x, 1, 3)
    assert not check_cardinality(self.x, 0, 2)

    self = T([])
    assert check_cardinality(self.x, 0, None)
    assert check_cardinality(self.x, 0, 3)
    assert not check_cardinality(self.x, 1, None)


def test_join_no_sep():
    assert join([1,2,3], ) == '123'


def test_join_no_sep2():
    assert join([1,2,3]) == '123'


def test_join_sep():
    assert join([1,2,3], ',') == '1,2,3'


def test_contains():
    assert contains([1, 2, 3], [3, 1])


def test_doesnt_contains():
    assert not contains([1, 2, 3], [3, 1, 0])


def test_disjoint():
    assert disjoint([1, 2, 3], [4, 5])


def test_not_disjoint():
    assert not disjoint([1, 2, 3], [1, 4, 5])


if __name__ == "__main__":
    test_multiprop()
    test_multiprop_int()
    test_check_cardinality_1_1()
    test_check_cardinality_0_1()
    test_check_cardinality_list()

# EOF
