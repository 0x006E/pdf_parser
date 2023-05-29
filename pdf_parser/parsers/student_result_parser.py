import re

from .row_parser import RowParser
from ..exceptions import InvalidRegisterNumberError


class StudentResultParser(RowParser):
    REGISTER_PATTERN = r'(L?)(?P<college>[A-Z]{3})(?P<year>[0-9]{2})(?P<branch>[A-Z]{2})(?P<serial>[0-9]{3})'
    RESULT_PATTERN = r'^(?P<subcode>[^(]+)\s*\((?P<grade>[^)]+)\)$'

    def __init__(self):
        super().__init__(self.REGISTER_PATTERN)

    def parse_row(self, row):
        register_info = super().parse_row(row)
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
            register_info["lateral_entry"] = register_info["lateral"] == "L"
            cleaned_row = re.sub(r'[\n\s]+', '', row)
            sublist = cleaned_row.split(',')
            subjects = [re.match(self.RESULT_PATTERN, x).groupdict()
                        for x in sublist]
            return {"register_info": register_info, "subjects": subjects}
        return None
