from dollar import dollar


def test_multiplication():
    d = dollar.Dollar(5)
    product = d.times(2)
    assert 10 == product.amount

    product = d.times(3)
    assert 15 == product.amount


def test_equality():
    assert dollar.Dollar(5) == dollar.Dollar(5)
    assert dollar.Dollar(5) != dollar.Dollar(6)
