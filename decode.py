import sys


def bin_keys(max_length=7):
    length = 1
    while length <= max_length:
        fstring = '{:0' + str(length) + 'b}'
        for i in range(2**length - 1):
            yield fstring.format(i)

        length += 1


def make_header_map(header):
    return dict((k, v) for k, v in zip(bin_keys(), header))


def decode(header, message):
    # strip anything illegal from the message
    message = "".join([c for c in message if c in ('0', '1')])
    header_map = make_header_map(header)
    decoded = []

    def extract_segment(message):
        segment = []
        size, message = message[0:3], message[3:]
        size = int(size, 2)

        if size == 0:
            # we've reached '000', the termination string
            return ([], "")

        key, message = message[0:size], message[size:]
        while int(key, 2) != (2**(size) - 1):  # while the key isn't all ones
            segment.append(key)
            key, message = message[0:size], message[size:]

        return segment, message

    keep_going = True
    while keep_going:
        segment, message = extract_segment(message)
        if not message:
            keep_going = False

        decoded.extend([header_map[key] for key in segment])

    return "".join(decoded)


def find_last_header_char(s):
    return max([(i, c) for i, c in enumerate(s) if c not in ('0, 1')])


def process_line(line):
    line = line.strip()
    if not line:
        return

    pos, _ = find_last_header_char(line)
    pos += 1
    header, message = line[0:pos], line[pos:]
    print(decode(header, message))


def test():
    line = '$#**\\0100000101101100011100101000'
    process_line(line)

if __name__ == '__main__':
    with open(sys.argv[1]) as lines:
        for line in lines:
            process_line(line)
