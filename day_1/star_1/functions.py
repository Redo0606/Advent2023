import re

def get_input_lines(file) : 
    with open(file, 'r') as file:
        return [line for line in file]

def get_first_and_last_digit(line) : 
    pattern = "[0-9]"
    matches = re.findall(pattern=pattern, string=line)
    return matches[0], matches[len(matches)-1]

def compute_total(lines) : 
    sum = 0
    for line in lines :
         left, right = get_first_and_last_digit(line=line)
         if left and right : 
            sum += int(f"{left}{right}")
    return sum