import utils
import re


def lenDec(s, cre):
    m = sum(len(re.findall(c[0], s)) * c[1] for c in cre)
    return len(s) - m


def lenEnc(s, cre):
    m = sum(len(re.findall(c[0], s)) * c[1] for c in cre)
    return 2 + len(s) + m


data = utils.get_input(2015, 8).split("\n")[:-1]
num_string_literals = sum(len(s) for s in data)
print(num_string_literals)


cre = [
    (re.compile(r"(\\\")"), 1),
    (re.compile(r"(\\x[0-9a-f][0-9a-f])"), 3),
    (re.compile(r"(\\\\)"), 1)
]

num_in_memory = sum(lenDec(s[1:-1], cre) for s in data)
print(f"Part 1: {num_string_literals - num_in_memory}")

cre = [
    (re.compile(r"(\\)"), 1),
    (re.compile(r"(\")"), 1)
]

num_encoded = sum(lenEnc(s, cre) for s in data)

print(f"Part 2: {num_encoded - num_string_literals}")
