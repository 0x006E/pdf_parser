import re


class RowParser:
    def __init__(self, pattern):
        self.pattern = pattern

    def parse_row(self, row):
        match = re.match(self.pattern, row)
        if match:
            return match.groupdict()
        return None
