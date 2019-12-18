import utils


data = utils.get_input(2015, 3)
starting_pos = (0, 0)
moves = {
    "<": (-1, 0),
    ">": (1, 0),
    "^": (0, 1),
    "v": (0, -1)
}

visited = set()
pos = starting_pos
visited.add(pos)
for d in data:
    m = moves[d]
    pos = (pos[0] + m[0], pos[1] + m[1])
    visited.add(pos)

print(f"Part 1: visited {len(visited)} houses.")

visited = set()
turn = False
pos = starting_pos
robo_pos = starting_pos
visited.add(pos)
for d in data:
    m = moves[d]
    curr = None
    if turn:
        curr = (pos[0] + m[0], pos[1] + m[1])
        pos = curr
    else:
        curr = (robo_pos[0] + m[0], robo_pos[1] + m[1])
        robo_pos = curr

    turn = not turn

    visited.add(curr)

print(f"Part 2: visited {len(visited)} houses.")
