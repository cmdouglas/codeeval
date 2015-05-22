import sys
from itertools import product

def is_ugly(n):
    if n == 0:
        return True

    for i in (2, 3, 5, 7):
        if n % i == 0:
            return True

    return False


def compute_combination(ops, digits, ndigits):
    value = 0
    num_str = ''
    for i, digit in enumerate(digits):
        op = None
        num_str += digit
        if i < ndigits-1:
            op = ops[i]
        
        if op and op != ' ':
            value += int(num_str)
            num_str = op
        
    value += int(num_str)
    return value
        

def count_ugly_combinations(digits):
    num_ugly = 0
    for ops in product(' +-', repeat=len(digits) - 1):
        value = compute_combination(ops, digits, len(digits))
        if value == 0 or value % 2 == 0 or value % 3 == 0 or value % 5 == 0 or value % 7 == 0:
            num_ugly += 1
        
    return num_ugly

def test():
    for digits in ["1", "9", "011", "12345"]:
        print(count_ugly_combinations(digits))

def process_line(line):
    line = line.strip()
    if not line:
        return
    
    print(count_ugly_combinations(line))
    
if __name__ == '__main__':
    with open(sys.argv[1]) as lines:
        for line in lines:
            process_line(line)