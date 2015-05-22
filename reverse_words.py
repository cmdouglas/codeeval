import sys


def process_line(line):
    words = line.split(' ')
    print(' '.join(reversed(words)))


if __name__ == '__main__':
    with open(sys.argv[1]) as lines:
        for line in lines:
            if line.strip():
                process_line(line)
