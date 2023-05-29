import re

from pdf_parser.parsers.row_parser import RowParser
from pdf_parser.exceptions import InvalidRegisterNumberError, InvalidSubjectCodeError


class StudentResultParser(RowParser):
    REGISTER_PATTERN = r'(L?)(?P<college>[A-Z]{3})(?P<year>[0-9]{2})(?P<branch>[A-Z]{2})(?P<serial>[0-9]{3})'
    SUBCODE_PATTERN = r'^(?P<subcode>[^(]+)\s*\((?P<grade>[^)]+)\)$'

    def __init__(self):
        super().__init__(self.REGISTER_PATTERN)

    def parse_row(self, row):
        register_info = super().parse_row(row[0])
        if register_info:
            if any(value is None for value in register_info.values()):
                missing_fields = []
                if register_info["year"] is None:
                    missing_fields.append("year")
                if register_info["branch"] is None:
                    missing_fields.append("branch")
                if register_info["college"] is None:
                    missing_fields.append("college")
                if register_info["serial"] is None:
                    missing_fields.append("serial number")
                error_message = f"Missing {', '.join(missing_fields)} in register number: {row}"
                raise InvalidRegisterNumberError(error_message)
            register_info["lateral_entry"] = row[0][0] == 'L'
            subjects = self.__parse_subjects(row[1])
            return {"register_info": register_info, "register_number": row[0], "subjects": subjects}
        return None

    def __parse_subjects(self, sub):
        cleaned_row = re.sub(r'[\n\s]+', '', sub)
        sublist = cleaned_row.split(',')
        subjects = []
        for subject_string in sublist:
            try:
                subject = self.__parse_subject_code(subject_string)
                subjects.append(subject)
            except InvalidSubjectCodeError as e:
                print(str(e))
                pass
        return subjects

    def __parse_subject_code(self, subject_string):
        try:
            match = re.match(self.SUBCODE_PATTERN, subject_string)
            if match:
                return match.groupdict()
            else:
                raise InvalidSubjectCodeError(f"Invalid subject code - {match.string}")
        except Exception as e:
            raise InvalidSubjectCodeError("Error parsing subject code") from e
