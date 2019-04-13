"""Custom Exception module."""


class TypeNotSupportedError(Exception):
    """Raised when a non-acceptable data is passed."""
    pass  # pylint: disable=W0107


class NonNumericTypeNotSupportedError(TypeNotSupportedError):
    """Raised when a non-numeric data is passed."""
    pass  # pylint: disable=W0107


class InvalidDataError(Exception):
    """Raised when an invalid data is passed."""
    pass  # pylint: disable=W0107
