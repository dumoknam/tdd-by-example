class Money(object):
    """Parent class"""
    def __init__(self, amount):
        super(Money, self).__init__()
        self._amount = amount

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)


class Franc(Money):
    """Franc"""
    def times(self, multiplier):
        return Franc(self._amount * multiplier)



class Dollar(Money):
    """Dollar"""
    def times(self, multiplier):
        return Dollar(self._amount * multiplier)
