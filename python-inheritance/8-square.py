"""
    The documentation includes descriptions of the classes, their attribut.
      It provides information on what each class represents, what each a,
       and what each method does. The parameters, return types, and ra.
"""


class BaseGeometry:
    """
    A base class for geometrical operations.

    Methods:
        integer_validator(self, name, value): Validates if a v
    """

    def integer_validator(self, name, value):
        """
        Validate if a value is an integer greater than zero.

        Parameters:
            name (str): The name of the value being validated.
            value (int): The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to zero.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
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
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def __str__(self):
        """
        Return a string representation of the rectangle.

        Returns:
            str: The string representation of the rectangle in the ".
        """
        return f"[Rectangle] {self.__width}/{self.__height}"

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            int: The calculated area of the rectangle.
        """
        return self.__width * self.__height


class Square(Rectangle):
    """
    A class representing a square, which is a
    Inherits from:
        Rectangle

    Attributes:
        __size (int): The size of the square (width and h.
    """

    def __init__(self, size):
        """
        Initialize a square with the given size.

        Parameters:
            size (int): The size of the square.
        """
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """
        Return a string representation of the square.

        Returns:
            str: The string representation of the square in the format "".
        """
        return f"[Square] {self.__size}/{self.__size}"
