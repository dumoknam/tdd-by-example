
class Dollar(object):
	"""docstring for Dollar"""
	def __init__(self, amount):
		super(Dollar, self).__init__()
		self.amount = amount
	
	def times(self, multiplier):
		return Dollar(self.amount * multiplier)
