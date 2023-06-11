import dpath


def update_student_details(data, final_data):
    intermediate_dict = {}
    register_info = data['register_info']
    subjects = data['subjects']
    register_number = data['register_number']

    # Extract relevant information from register_info
    branch = register_info['branch']
    year = register_info['year']
    lateral_entry = register_info['lateral_entry']

    # Create path to the branch
    branch_path = f"years/'{year}'/branches/{branch}"

    # Set branch code and name in final_data
    dpath.new(intermediate_dict, branch_path + "/name", None)

    # Set subject codes and names in final_data
    for subject in subjects:
        subject_code = subject['subcode']
        matches = list(dpath.search(final_data, "subjects/" + subject_code))
        if matches:
            continue
        dpath.new(intermediate_dict, "subjects/" + subject_code, None)

    # Create path to the student
    student_path = branch_path + "/students/0"

    # Set student register number in final_data
    dpath.new(intermediate_dict, student_path + "/register_number", register_number)
    
    # Set additional register ingo in final_data
    dpath.new(intermediate_dict, student_path + "/register_info", register_info)

    # Set student lateral entry status in final_data
    dpath.new(intermediate_dict, student_path + "/lateral_entry", lateral_entry)

    # Set subjects and grades for the student
    for subject in subjects:
        subject_code = subject['subcode']
        grade = subject['grade']
        dpath.new(intermediate_dict, student_path + f"/subjects/{subject_code}", grade)

    return dpath.merge(final_data, intermediate_dict)


def add_subject_name(subject_code, subject_name, final_data):
    subjects = final_data.get('subjects', {})
    subjects[subject_code] = subject_name
    final_data['subjects'] = subjects
    return final_data
