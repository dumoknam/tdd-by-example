from money import (
    dollar,
    franc,
)


def test_multiplication():
    d = dollar.Dollar(5)
    assert dollar.Dollar(10) == d.times(2)
    assert dollar.Dollar(15) == d.times(3)


def test_equality():
    assert dollar.Dollar(5) == dollar.Dollar(5)
    assert dollar.Dollar(5) != dollar.Dollar(6)


def test_franc_multiplication():
    f = franc.Franc(5)
    assert franc.Franc(10) == f.times(2)
    assert franc.Franc(15) == f.times(3)
