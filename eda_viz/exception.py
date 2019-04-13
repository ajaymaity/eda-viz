"""Custom Exception module."""


class TypeNotSupportedError(Exception):
    """Raised when a non-acceptable data is passed."""
    pass


class NonNumericTypeNotSupportedError(TypeNotSupportedError):
    """Raised when a non-numeric data is passed."""
    pass


class InvalidDataError(Exception):
    """Raised when an invalid data is passed."""
    pass
