"""
    bclidiugfvbw voihfv 
"""

from models.base import Base

class Rectangle(Base):
    """
        NCB DVB KHFCN;V M;BV
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        NCB DVB KHFCN;V M;BV
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        NCB DVB KHFCN;V M;BV
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        NCB DVB KHFCN;V M;BV
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        NCB DVB KHFCN;V M;BV
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        NCB DVB KHFCN;V M;BV
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        NCB DVB KHFCN;V M;BV
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        NCB DVB KHFCN;V M;BV
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        NCB DVB KHFCN;V M;BV
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        NCB DVB KHFCN;V M;BV
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        NCB DVB KHFCN;V M;BV
        """
        return self.__width * self.__height

    def display(self):
        """
        NCB DVB KHFCN;V M;BV
        """
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """
        NCB DVB KHFCN;V M;BV
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """
        NCB DVB KHFCN;V M;BV
        """
        if args:
            attributes = ['id', 'width', 'height', 'x', 'y']
            for i, arg in enumerate(args):
                setattr(self, attributes[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)