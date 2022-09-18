class Error(Exception):
    """
    Base class for exception
    """
    pass

class ValueNotFound(Error):
    """
    Raised when given value is not found in table
    """
    pass

class ValueDuplicate(Error):
    """
    Raised when given value is duplicate and cannot be inserted into table
    """
    pass