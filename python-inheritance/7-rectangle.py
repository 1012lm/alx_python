"""
    The updated code snippet defines a Rectangle class. 
    It has an __init__ method for initializing the width and height of the rectangle, 
    and it performs validation using the integer_validator method.
      The __str__ method returns a string representation of the rectangle.
        The area method calculates the area of the rectangle by multiplying its width and height.
      The integer_validator method is also included for validating integer values.
"""

class Rectangle:
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
            str: The string representation of the rectangle in the format "[Rectangle] width/height".
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            int: The calculated area of the rectangle.
        """
        return self.__width * self.__height

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
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))