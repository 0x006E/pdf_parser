import dpath.util


def update_student_details(data, final_data):
    register_info = data['register_info']
    subjects = data['subjects']
    register_number = data['register_number']

    # Extract relevant information from register_info
    branch = register_info['branch']
    year = register_info['year']
    lateral_entry = register_info['lateral_entry']

    # Create path to the branch
    branch_path = f"years/{year}/branches/{branch}"

    # Set branch code and name in final_data
    dpath.util.new(final_data, branch_path + "/code", branch)
    dpath.util.new(final_data, branch_path + "/name", None)

    # Set subject codes and names in final_data
    for subject in subjects:
        subject_code = subject['subcode']
        dpath.util.new(final_data, branch_path + "/subjects/" + subject_code + "/code", subject_code)

    # Create path to the student
    student_path = branch_path + f"/students/{register_number}"

    # Set student register number in final_data
    dpath.util.new(final_data, student_path + "/register_number", register_number)

    # Set student lateral entry status in final_data
    dpath.util.new(final_data, student_path + "/lateral_entry", lateral_entry)

    # Set subjects and grades for the student
    for subject in subjects:
        subject_code = subject['subcode']
        grade = subject['grade']
        dpath.util.new(final_data, student_path + f"/subjects/{subject_code}/subcode", subject_code)
        dpath.util.new(final_data, student_path + f"/subjects/{subject_code}/grade", grade)

    return final_data


def replace_subject_name(final_data, subject_code, subject_name):
    subject_paths = dpath.util.search(final_data, '/*/subjects/*/code')

    for path, subject_code_match in subject_paths:
        if subject_code_match == subject_code:
            subject_name_path = path.replace('/code', '/name')
            dpath.util.set(final_data, subject_name_path, subject_name)

    return final_data
