"""
    The documentation includes descriptions of the classes, their attribut.
      It provides information on what each class represents, what each a,
       and what each method does. The parameters, return types, and ra.
"""

#!/usr/bin/python3
"""
Module 8-square
Defines the Square class
"""

Rectangle = __import__('7-rectangle').Rectangle


class Square(Rectangle):
    """
    Represents a square, inherits from Rectangle.
    """

    def __init__(self, size):
        """
        Initializes a Square instance.
        Args:
            size (int): The size of the square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """
        Returns a string representation of the Square instance.
        """
        return "[Square] {}/{}".format(self.__width, self.__width)
