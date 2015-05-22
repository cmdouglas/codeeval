
def permutations(l):
    if len(l) <= 1:
        return [l]

    r = []
    for fixed in l:
        new_l = l[:]
        new_l.remove(fixed)

        for p in permutations(new_l):
            p.insert(0, fixed)
            r.append(p)

    return r


def process_line(line):
    line = line.strip()
    if not line:
        return
    l = list(line)
    perms = sorted(permutations(l))

    print(",".join(["".join(perm) for perm in perms]))


if __name__ == '__main__':
    import sys
    with open(sys.argv[1]) as lines:
        for line in lines:
            process_line(line)
