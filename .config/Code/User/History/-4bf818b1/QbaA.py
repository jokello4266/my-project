import re 

file_path = "/var/log"

def parse_log(file_path):
    with open(file_path, 'r') as file:
        log_data = file.read()
    pattern = re.compile_r(r'ERROR:(.*)')
    errors = pattern.findall(log_data)
    return errors

errors = parse_log('application.log')
for error in errors:
    print(errors)


