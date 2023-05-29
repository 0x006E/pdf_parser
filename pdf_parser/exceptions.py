class PDFParsingError(Exception):
    """Exception raised when an error occurs during PDF parsing."""


class InvalidPDFError(Exception):
    """Exception raised when the provided PDF is invalid or cannot be parsed."""
