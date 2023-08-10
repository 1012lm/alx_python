"""
bxsuafvtbv=o kaednbfv ewsfdcxv;jn q
"""

from models.base import Base

class Rectangle(Base):
    """
    cabd slfvo;awhnfsc alv 
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
         bd cvo;sfcqjwdbv z;cfcwsafcje]q[wse-dc]
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
            mbdlxfiuval;rdfov
        """
        return self.__width

    @width.setter
    def width(self, value):
         """
            mbdlxfiuval;rdfov
        """
         self.__width = value

    @property
    def height(self):
         """
            mbdlxfiuval;rdfov
        """
         return self.__height

    @height.setter
    def height(self, value):
         """
            mbdlxfiuval;rdfov
        """
         self.__height = value

    @property
    def x(self):
         """
            mbdlxfiuval;rdfov
        """
         return self.__x

    @x.setter
    def x(self, value):
         """
            mbdlxfiuval;rdfov
        """
         self.__x = value

    @property
    def y(self):
         """
            mbdlxfiuval;rdfov
        """
         return self.__y

    @y.setter
    def y(self, value):
         """
            mbdlxfiuval;rdfov
        """
         self.__y = value