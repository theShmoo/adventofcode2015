import utils
import re
import copy


rshift_re = re.compile(r"(.+) RSHIFT ([0-9]+) -\> (.+)")
lshift_re = re.compile(r"(.+) LSHIFT ([0-9]+) -\> (.+)")
or_re = re.compile(r"(.+) OR (.+) -\> (.+)")
and_re = re.compile(r"(.+) AND (.+) -\> (.+)")
number_and_re = re.compile(r"([0-9]+) AND (.+) -\> (.+)")
not_re = re.compile(r"NOT (.+) -\> (.+)")
assign_number_re = re.compile(r"([0-9]+) -\> (.+)")
assign_wire_re = re.compile(r"(.+) -\> (.+)")

operations = {}
cache = {}


def access(operartions, cache, i):
    if i not in cache:
        cache[i] = operations[i]()
    return cache[i]


data = utils.get_input(2015, 7).split("\n")[:-1]
for d in data:
    m = re.match(rshift_re, d)
    if m:
        g = m.groups()
        operations[g[2]] = lambda a=g[0], b=int(g[1]): access(
            operations, cache, a) >> b
        continue

    m = re.match(lshift_re, d)
    if m:
        g = m.groups()
        operations[g[2]] = lambda a=g[0], b=int(g[1]): access(
            operations, cache, a) << b
        continue

    m = re.match(or_re, d)
    if m:
        g = m.groups()
        operations[g[2]] = lambda a=g[0], b=g[1]: access(
            operations, cache, a) | access(operations, cache, b)
        continue

    m = re.match(number_and_re, d)
    if m:
        g = m.groups()
        operations[g[2]] = lambda a=int(g[0]), b=g[1]: a & access(
            operations, cache, b)
        continue

    m = re.match(and_re, d)
    if m:
        g = m.groups()
        operations[g[2]] = lambda a=g[0], b=g[1]: access(
            operations, cache, a) & access(operations, cache, b)
        continue

    m = re.match(not_re, d)
    if m:
        g = m.groups()
        operations[g[1]] = lambda a=g[0]: ~access(operations, cache, a)
        continue

    m = re.match(assign_number_re, d)
    if m:
        g = m.groups()
        cache[g[1]] = int(g[0])
        continue

    m = re.match(assign_wire_re, d)
    if m:
        g = m.groups()
        operations[g[1]] = lambda a=g[0]: access(operations, cache, a)
        continue


cache_copy = copy.copy(cache)

v = operations['a']()
print(f"Part 1: {v}")

cache = cache_copy
cache['b'] = v

v2 = operations['a']()
print(f"Part 2: {v2}")
