import re 
import camelot

tables = camelot.read_pdf('/content/drive/MyDrive/result_MES (2).pdf', pages='1-end')

df = tables
def is_regno(string):
    m = re.match(r'(L?)(?P<college>[A-Z]{3})(?P<year>[0-9]{2})(?P<branch>[A-Z]{2})(?P<Serialno>[0-9]{3})',string)
    return m
def result(string):
    m = re.match(r'^(?P<subcode>[^(]+)\s*\((?P<grade>[^)]+)\)$', string)
    return m
def which_branch(string):
    m = re.match(r'(L?)(?P<college>[A-Z]{3})(?P<year>[0-9]{2})(?P<branch>[A-Z]{2})(?P<Serialno>[0-9]{3})',string)
    if m:
        branch = m.group('branch')
        return branch
    else:
        return "error"

for table in df:
    for index,row in table.df.iterrows():
        regno = is_regno(row[0])

        if regno:
            cleanstring = re.sub('[\n\s]+', '', row[1])
            sublist = cleanstring.split(',')
            student_result = [result(x).groupdict() for x in sublist]
            individual = {"regno": "".join(regno.groupdict().values()), "subjects": student_result}
            #print(individual)
            register_no = individual["regno"]
            branch = which_branch(register_no)
            print(branch)
        
            
        else:
            print(regno)
