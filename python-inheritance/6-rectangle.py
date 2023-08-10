"""
    The code snippet provided defines two classes: BaseGeometry and Rectangle.
    """


BaseGeometry = __import__('5-base_geometry.py').BaseGeometry


class Rectangle(BaseGeometry ):
    """
    A class representing a rectangle.

    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.
    """
    def __init__(self, width, height):
        """
        Initialize a rectangle with the given width and height.

        Parameters:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """
        Return a string representation of the rectangle.

        Returns:
            str: The string representation of the rectangle in the format "[Rectangle] width/height".
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def __dir__(self):
        """
        Return a list of attributes and methods of the Rectangle class.

        Returns:
            list: A list of attributes and methods.
        """
        return [
            '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', 
            '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', 
            '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__',
            '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__',
            'area', 'integer_validator'
        ]