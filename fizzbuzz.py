import sys


def fizzbuzz_sequence(fizz, buzz, total):
    for i in range(1, total + 1):
        if (i % fizz == 0) and (i % buzz == 0):
            yield 'FB'
        elif i % fizz == 0:
            yield 'F'
        elif i % buzz == 0:
            yield 'B'
        else:
            yield str(i)


def process_line(l):
    fizz, buzz, total = l.split(' ')
    fizz = int(fizz)
    buzz = int(buzz)
    total = int(total)

    print(" ".join(fizzbuzz_sequence(fizz, buzz, total)))


if __name__ == '__main__':
    with open(sys.argv[1]) as lines:
        for line in lines:
            if not line.strip():
                continue
            process_line(line)
