class InvalidValueException(ValueError):
    def __init__(self, message="Value can not be zero or negative."):
        super().__init__(message)

