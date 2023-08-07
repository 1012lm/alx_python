"""
    Check if an object is an instance of a given class or a subclass of it.

    Parameters:
        obj (object): The object to check.
        a_class (class): The class to compare against.

    Returns:
        bool: True if the object is an instance of the given class or a subclass of it, False otherwise.
    """
def is_kind_of_class(obj, a_class):
    """
    Check if an object is an instance of a given class or a subclass of it.

    Parameters:
        obj (object): The object to check.
        a_class (class): The class to compare against.

    Returns:
        bool: True if the object is an instance of the given class or a subclass of it, False otherwise.
    """
    return isinstance(obj, a_class)