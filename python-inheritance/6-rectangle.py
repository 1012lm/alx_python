"""
    The code snippet provided defines two classes: BaseGeometry and Rectangle.
"""
#!/usr/bin/python3
"""
Module 6-rectangle
Defines the Rectangle class
"""

BaseGeometry = __import__('5-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Represents a rectangle, inherits from BaseGeometry.
    """

    def __init__(self, width, height):
        """
        Initializes a Rectangle instance.
        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """
        Returns a string representation of the Rectangle instance.
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """
        Calculates the area of the Rectangle instance.
        Returns:
            The area of the rectangle.
        """
        return self.__width * self.__height
