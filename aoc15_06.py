import utils


def parseCoordinates(coord):
    pairs = coord.split(" through ")
    f = pairs[0].split(",")
    t = pairs[1].split(",")
    return ((int(f[0]), int(f[1])), (int(t[0]), int(t[1])))


def switchLights(f, t, grid, command):
    for x in range(f[0], t[0] + 1):
        for y in range(f[1], t[1] + 1):
            grid[x][y] = command(x, y)


def numLightsOn(grid):
    s = 0
    for y in range(len(grid)):
        s += grid[y].count(True)
    return s


def totalBrightness(grid):
    s = 0
    for y in range(len(grid)):
        s += sum(grid[y])
    return s


grid_size = 1000
grid = [[False] * grid_size for _ in range(grid_size)]
data = utils.get_input(2015, 6).split("\n")[:-1]
# data = ["toggle 0,0 through 999,0"]
for line in data:
    if line.startswith("turn on"):
        f, t = parseCoordinates(line[8:])
        switchLights(f, t, grid, lambda x, y: True)
    elif line.startswith("toggle"):
        f, t = parseCoordinates(line[7:])
        switchLights(f, t, grid, lambda x, y: not grid[x][y])
    elif line.startswith("turn off"):
        f, t = parseCoordinates(line[9:])
        switchLights(f, t, grid, lambda x, y: False)


print(f"Part 1: {numLightsOn(grid)} lights are turned on")

grid = [[0] * grid_size for _ in range(grid_size)]
for line in data:
    if line.startswith("turn on"):
        f, t = parseCoordinates(line[8:])
        switchLights(f, t, grid, lambda x, y: grid[x][y] + 1)
    elif line.startswith("toggle"):
        f, t = parseCoordinates(line[7:])
        switchLights(f, t, grid, lambda x, y: grid[x][y] + 2)
    elif line.startswith("turn off"):
        f, t = parseCoordinates(line[9:])
        switchLights(f, t, grid, lambda x, y: max(grid[x][y] - 1, 0))

print(f"Part 2: {totalBrightness(grid)} Brightness")
