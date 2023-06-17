import camelot
import logging
from pdf_parser.exceptions import PDFParsingError
from pdf_parser.parsers.student_result_parser import StudentResultParser
from pdf_parser.parsers.subject_details_parser import SubjectDetailsParser
from pdf_parser.utils.conversion_backend import ConversionBackend
from pdf_parser.utils.data_utils import update_student_details, add_subject_name

def parse_pdf(file_path, pages="1-end", final_data={}):
    logger = logging.getLogger('pdf_parser')
    logger.info("Running parser")

    try:
        tables = camelot.read_pdf(file_path, pages='1-end', backend=ConversionBackend())
    except Exception as error:
        raise PDFParsingError(f"Error parsing PDF: {str(error)}") from error

    student_parser = StudentResultParser()
    subject_details_parser = SubjectDetailsParser()
    num_tables = str(len(tables))
    logger.info("Found %s tables in file", num_tables)
    for index, table in enumerate(tables):
        logger.info("Parsing table: %s/%s", str(index), num_tables)
        for _, row in table.df.iterrows():
            result = student_parser.parse_row(row)
            subcode = subject_details_parser.parse_row(row)
            if result:
                final_data = update_student_details(result, final_data)
                logger.debug("Found result record. Adding to dictionary")
            elif subcode:
                final_data = add_subject_name(subcode['code'], subcode['name'], final_data)
                logger.debug("Found subject record. Adding to dictionary")
    logger.info("Parsing done. exiting")
    return final_data


