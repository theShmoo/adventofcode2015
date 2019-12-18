import utils


data = utils.get_input(2015, 1)
depth = 0
for i, c in enumerate(data):
    depth += 1 if c == '(' else -1

print(f"Part 1: {depth}")

for i, c in enumerate(data):
    depth += 1 if c == '(' else -1
    if depth < 0:
        position = i + 1
        print(f"Part 2: {position}")
        break
