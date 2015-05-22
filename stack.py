def process_ints(ints):
    i = 0
    while True:
        if not ints:
            return

        n = ints.pop()
        if i % 2 == 0:
            yield n

        i += 1


def process_line(line):
    line = line.strip()
    ints = [i for i in line.split(" ")]

    print(" ".join(process_ints(ints)))


if __name__ == '__main__':
    import sys
    with open(sys.argv[1]) as lines:
        for line in lines:
            process_line(line)
