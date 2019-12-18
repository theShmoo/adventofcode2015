import utils
from itertools import combinations


data = utils.get_input(2015, 2).split("\n")

wrapping_total = 0
ribbon_total = 0

for d in data[:-1]:
    dims = [int(i) for i in d.split("x")]
    areas = [a * b for a, b in combinations(dims, 2)]
    wrapping = 2 * sum(areas) + min(areas)
    wrapping_total += wrapping

    perimeters = [2 * (a + b) for a, b in combinations(dims, 2)]
    bow = dims[0] * dims[1] * dims[2]
    ribbon = bow + min(perimeters)
    ribbon_total += ribbon


print(f"Part 1: {wrapping_total} feet of wrapping paper")
print(f"Part 2: {ribbon_total} feet of ribbon")
