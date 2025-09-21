class EmptyCartException(Exception):
    def __init__(self, message="Cart is Empty. Can not proceed to checkout."):
        super().__init__(message)
