import utils
import re
import itertools


data = utils.get_input(2015, 9).split("\n")[:-1]
re_in = re.compile(r"(.+) to (.+) = ([0-9]+)")
edges = {}

for line in data:
    m = re.match(re_in, line)
    g = m.groups()
    distance = int(g[2])

    if g[0] in edges:
        edges[g[0]][g[1]] = distance
    else:
        edges[g[0]] = {g[1]: distance}

    if g[1] in edges:
        edges[g[1]][g[0]] = distance
    else:
        edges[g[1]] = {g[0]: distance}

cities = list(edges.keys())


def calcPath(cities, edges):
    return sum(edges[cities[i - 1]][cities[i]] for i in range(1, len(cities)))


shortest_path = cities
shortest_quess = calcPath(shortest_path, edges)
longest_path = cities
longest_quess = shortest_quess

for p in itertools.permutations(cities):
    q = calcPath(p, edges)
    if q < shortest_quess:
        shortest_path = p
        shortest_quess = q
    if q > longest_quess:
        longest_path = p
        longest_quess = q

print(f"Part 1: shortes route: {shortest_path} distance {shortest_quess}")
print(f"Part 2: longest route: {longest_path} distance {longest_quess}")
