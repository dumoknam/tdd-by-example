from dollar import dollar

def test_multiplication():
	d = dollar.Dollar(5)
	d.times(2)
	assert 10 == d.amount