from money.money import (
    Dollar,
    Franc,
)


def test_multiplication():
    d = Dollar(5)
    assert Dollar(10) == d.times(2)
    assert Dollar(15) == d.times(3)


def test_equality():
    assert Dollar(5) == Dollar(5)
    assert Dollar(5) != Dollar(6)


def test_franc_multiplication():
    f = Franc(5)
    assert Franc(10) == f.times(2)
    assert Franc(15) == f.times(3)


def test_franc_equality():
    f = Franc(5)
    assert Franc(5) == Franc(5)
    assert Franc(5) != Franc(6)