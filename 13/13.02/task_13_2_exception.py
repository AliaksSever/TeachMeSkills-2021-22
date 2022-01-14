
class MyException(Exception):
    def __init__(self, message='Ups,something going wrong, probably invalid input, try again'):
        super().__init__(message)
