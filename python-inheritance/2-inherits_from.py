"""
    Check if an object inherits from a given class.
    """
def inherits_from(obj, a_class):  
    """
    Check if an object inherits from a given class.

    Parameters:
        obj (object): The object to check.
        a_class (class): The class to compare against.

    Returns:
        bool: True if the object inherits from the given class and is not an instance of it, False otherwise.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
