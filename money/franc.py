class Franc(object):
    """Franc"""
    def __init__(self, amount):
        super(Franc, self).__init__()
        self._amount = amount

    def times(self, multiplier):
        return Franc(self._amount * multiplier)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)
