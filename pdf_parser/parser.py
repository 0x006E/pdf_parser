import re
import camelot

REGNO_PATTERN = r'(L?)(?P<college>[A-Z]{3})(?P<year>[0-9]{2})(?P<branch>[A-Z]{2})(?P<Serialno>[0-9]{3})'
RESULT_PATTERN = r'^(?P<subcode>[^(]+)\s*\((?P<grade>[^)]+)\)$'

def extract_regno_from_string(string):
    m = re.match(REGNO_PATTERN, string)
    return m

def extract_result_from_string(string):
    m = re.match(RESULT_PATTERN, string)
    return m

def extract_branch_from_regno(regno):
    regno_match = extract_regno_from_string(regno)
    if regno_match:
        branch = regno_match.group('branch')
        return branch
    else:
        return "error"

def parse_pdf(file_path):
    tables = camelot.read_pdf(file_path, pages='1-end', flavor='stream')
    extracted_results = []
    for table in tables:
        for index, row in table.df.iterrows():
            regno = extract_regno_from_string(row[0])
            if regno:
                clean_string_row = re.sub('[\n\s]+', '', row[1])
                sublist = clean_string_row.split(',')
                student_result = [extract_result_from_string(x).groupdict() for x in sublist]
                individual = {"regno": "".join(regno.groupdict().values()), "subjects": student_result}
                extracted_results.append(individual)
    return extracted_results
