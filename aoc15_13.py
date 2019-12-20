import utils
import re
from itertools import permutations


data = utils.get_input(2015, 13)[:-1].split("\n")
# Alice would gain 54 happiness units by sitting next to Bob.
pattern = re.compile(r"(.+) would (.+) ([0-9]+) happiness units by sitting next to (.+)\.")

graph = {}

for line in data:
    m = re.match(pattern, line)
    if m:
        g = m.groups()
        sitter, op, val, neighbour = g[0], g[1], int(g[2]), g[3]
        if sitter not in graph:
            graph[sitter] = []
        if op == "lose":
            val = -val
        graph[sitter].append((neighbour, val))
    else:
        print(line)

for p in permutations(list(graph.keys)):
    for k in p:

