"""
This module defines a class called Square, which represents a square with a given size.

Attributes:
    __size (int): The size of the square.

"""

def is_same_class(obj, a_class):
    """
    This function checks if an object is an instance of a given class.

    Parameters:
        obj (object): The object to check.
        a_class (class): The class to compare against.

    Returns:
        bool: True if the object is an instance of the given class, False otherwise.
    """
    return type(obj) is a_class