import utils


data = utils.get_input(2015, 10)[:-1]

for t in range(50):
    print(t)
    result = ""
    seq = 1
    for i in range(1, len(data)):
        if data[i - 1] == data[i]:
            seq += 1
        else:
            result += str(seq) + data[i - 1]
            seq = 1
    result += str(seq) + data[-1]
    data = result
    if t == 39:
        print(f"Part 1: Length of string is {len(result)}")


print(f"Part 2: Length of string is {len(result)}")
