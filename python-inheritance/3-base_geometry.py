"""
    A base class for geometrical operations.
    """

class BaseGeometry:
    """
    A base class for geometrical operations.
    """
    def __str__(self):
        return "[BaseGeometry]"

    def __repr__(self):
        return "[BaseGeometry]"

    def __dir__(self):
        return [
            '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__',
            '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__',
            '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__',
            '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__',
            '__subclasshook__', '__weakref__'
        ]
    