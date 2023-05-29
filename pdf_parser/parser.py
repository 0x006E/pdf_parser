import camelot

from .exceptions import PDFParsingError
from .parsers.student_result_parser import StudentResultParser


def parse_pdf(file_path):
    try:
        tables = camelot.read_pdf(file_path, pages='1-end', flavor='stream')
    except Exception as error:
        raise PDFParsingError(f"Error parsing PDF: {str(error)}") from error

    student_parser = StudentResultParser()

    extracted_results = []
    for table in tables:
        for _, row in table.df.iterrows():
            result = student_parser.parse_row(row)
            if result:
                extracted_results.append(result)

    return extracted_results
