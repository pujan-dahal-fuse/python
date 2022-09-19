class Error(Exception):
    """
    Base class for exception
    """
    pass

class ValueNotFound(Error):
    """
    Raised when given value is not found in table
    """
    def __init__(self, msg=''):
        self.__msg__ = msg
    
    def message(self):
        return self.__msg__

class ValueDuplicate(Error):
    """
    Raised when given value is duplicate and cannot be inserted into table
    """
    def __init__(self, msg=''):
        self.__msg__ = msg
    
    def message(self):
        return self.__msg__