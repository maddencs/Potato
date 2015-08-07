__all__ = ['numbers']

class Field(object):
    def __init__(self, maximum=None, minimum=None, max_length=None, unique=False, null=False, default=None):
        self.maximum = maximum
        self.minimum = minimum
        self.max_length = max_length
        self.unique = unique
        self.default = default
        self.null = null
