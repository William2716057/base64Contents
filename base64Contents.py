import re
import base64

def is_base64(s):
    try:
        # string is multiple of 4
        if len(s) % 4 != 0:
            return False
        # decode the string
        base64.b64decode(s, validate=True)
        return True
    except Exception:
        return False

def find_base64_in_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        
    # regular expression to match potential base64 strings
    base64_pattern = r'(?:[A-Za-z0-9+/]{4}){2,}(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?'
    matches = re.findall(base64_pattern, content)
    
    # filter and print valid base64 strings
    for match in matches:
        if is_base64(match):
            print(f'Found possible base64: {match}')

file_path = 'sample.txt'
find_base64_in_file(file_path)