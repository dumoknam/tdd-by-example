from dollar import dollar


def test_multiplication():
    d = dollar.Dollar(5)
    assert dollar.Dollar(10) == d.times(2)
    assert dollar.Dollar(15) == d.times(3)


def test_equality():
    assert dollar.Dollar(5) == dollar.Dollar(5)
    assert dollar.Dollar(5) != dollar.Dollar(6)
