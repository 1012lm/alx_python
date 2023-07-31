class Square:
    """
    A class that defines a square by its size.
    """

    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class with an optional size parameter.

        Args:
            size (int): The size of the square. Default value is 0.
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Returns the current size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
            value (int): The new size of the square.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Computes and returns the area of the square.
        """
        return self.__size ** 2