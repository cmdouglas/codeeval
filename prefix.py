import sys


def compute(op, n1, n2):
    if op == '+':
        return n1 + n2
    elif op == '-':
        return n1 - n2
    elif op == '*':
        return n1 * n2
    elif op == '/':
        return n1 // n2


def evaluate_prefix(tokens):
    stack = []
    for token in reversed(tokens):
        if type(token) == int:
            stack.append(token)
        else:
            n1 = stack.pop()
            n2 = stack.pop()
            result = compute(token, n1, n2)
            stack.append(result)
    return stack.pop()


def process_line(line):
    operators = "+-*/"
    line = line.strip()
    tokens = []
    for s in line.split(" "):
        if s in operators:
            tokens.append(s)
        else:
            tokens.append(int(s))
    print(evaluate_prefix(tokens))


if __name__ == '__main__':
    with open(sys.argv[1]) as lines:
        for line in lines:
            if line.strip():
                process_line(line)
