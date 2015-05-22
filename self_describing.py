import sys
from collections import Counter


def is_self_describing(number):
    s = str(number)
    counts = Counter(s)
    for i, c in enumerate(s):
        if counts[str(i)] != int(c):
            return False
    return True


def process_line(line):
    if is_self_describing(line.strip()):
        print(1)
    else:
        print(0)

if __name__ == '__main__':
    with open(sys.argv[1]) as lines:
        for line in lines:
            if line.strip():
                process_line(line)
