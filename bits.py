def cmp_bits(n, p1, p2):
    return bool(n & 2**(p1-1)) == bool(n & 2**(p2-1))


def process_line(line):
    line = line.strip()
    if not line:
        return

    n, p1, p2 = [int(i) for i in line.split(',')]

    if cmp_bits(n, p1, p2):
        print("true")
    else:
        print("false")


if __name__ == '__main__':
    import sys
    with open(sys.argv[1]) as lines:
        for line in lines:
            process_line(line)
