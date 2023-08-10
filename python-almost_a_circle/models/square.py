"""
 xc c b cv hfcv 
"""

from models.rectangle import Rectangle

class Square(Rectangle):
    """
    bxo bsd;xcb kjbc
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        bxo bsd;xcb kjbc
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        bxo bsd;xcb kjbc
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        bxo bsd;xcb kjbc
        """
        self.width = value
        self.height = value

    def __str__(self):
        """
        bxo bsd;xcb kjbc
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)