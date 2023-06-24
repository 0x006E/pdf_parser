import re

from pdf_parser.parsers.row_parser import RowParser


class SubjectDetailsParser(RowParser):
    SUBJECTCODE_PATTERN = r'^(?P<subject_code>[A-Z]{3})(?P<subject_number>\d{3})$'


    def __init__(self):
        super().__init__(self.SUBJECTCODE_PATTERN)

    def parse_row(self, row):
        clean_subcode = self.__clean_string(row[0])
        subject_info = super().parse_row(clean_subcode)
        if subject_info:
            name = re.sub(r'[\n\s]+', ' ', row[1])
            return dict(code=clean_subcode, name=name.strip())
        else:
            return None

    @staticmethod
    def __clean_string(string: str) -> str:
        return re.sub(r'[\n\s]+', '', string)
