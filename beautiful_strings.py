import sys
from collections import Counter

letters = set("abcdefghijklmnopqrstuvwxyz")


def beauty(s):
    s = s.lower()
    s = "".join(c for c in s if c in letters)
    c = Counter(s)
    return sum(frequency*max_beauty for frequency, max_beauty in
               zip((num for letter, num in c.most_common()), range(26, 0, -1)))


def process_line(line):
    line = line.strip()
    if not line:
        return

    print(beauty(line))


if __name__ == '__main__':
    with open(sys.argv[1]) as lines:
        for line in lines:
            process_line(line)
