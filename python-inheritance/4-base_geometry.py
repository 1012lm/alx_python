"""
    A base class for geometrical operations.

    Methods:
        area(self): Raises an exception indicating that the method is not implemented.
    """

class BaseGeometry:
    """
    A base class for geometrical operations.

    Methods:
        area(self): Raises an exception indicating that the method is not implemented.
    """
    
    def __dir__(bg):
        return [
           '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__',
             '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__',
               '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', 
               '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'area'
        ]
    def area(self):
        """
        Calculate the area of the geometry.

        Raises:
            Exception: Indicates that the method is not implemented.
        """
        raise Exception("area() is not implemented")