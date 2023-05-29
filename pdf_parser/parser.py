import camelot

from pdf_parser.exceptions import PDFParsingError
from pdf_parser.parsers.student_result_parser import StudentResultParser
from pdf_parser.utils.conversion_backend import ConversionBackend
from pdf_parser.utils.data_utils import update_student_details, replace_subject_name


def parse_pdf(file_path):
    final_data = {}
    try:
        tables = camelot.read_pdf(file_path, pages='1-end', backend=ConversionBackend())
    except Exception as error:
        raise PDFParsingError(f"Error parsing PDF: {str(error)}") from error

    student_parser = StudentResultParser()


    for table in tables:
        for _, row in table.df.iterrows():
            result = student_parser.parse_row(row)
            if result:
                final_data = update_student_details(result, final_data)

    return final_data


pdf_file_path = 'r.pdf'
results = parse_pdf(pdf_file_path)
print(results)
