class PDFParsingError(Exception):
    """Exception raised when an error occurs during PDF parsing."""


class InvalidRegisterNumberError(Exception):
    """Exception raised when the provided PDF is invalid or cannot be parsed."""

class InvalidSubjectCodeError(Exception):
    """Exception raised when the provided subject code is malformed"""