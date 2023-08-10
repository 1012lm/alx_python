"""
    nvfilawufujvcjvh;awd
    dfnco;sc
"""

from models.base import Base

class Rectangle(Base):
    """
    nbd gb ;wirobgf kjhgvd
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
    nbd gb ;wirobgf kjhgvd
    """
        return self.__width

    @width.setter
    def width(self, value):
        """
    nbd gb ;wirobgf kjhgvd
    """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
    nbd gb ;wirobgf kjhgvd
    """
        return self.__height

    @height.setter
    def height(self, value):
        """
    nbd gb ;wirobgf kjhgvd
    """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
    nbd gb ;wirobgf kjhgvd
    """
        return self.__x

    @x.setter
    def x(self, value):
        """
    nbd gb ;wirobgf kjhgvd
    """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
    nbd gb ;wirobgf kjhgvd
    """
        return self.__y

    @y.setter
    def y(self, value):
        """
    nbd gb ;wirobgf kjhgvd
    """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
    nbd gb ;wirobgf kjhgvd
    """
        return self.__width * self.__height

    def display(self):
        """
    nbd gb ;wirobgf kjhgvd
    """
        for _ in range(self.__height):
            print("#" * self.__width)