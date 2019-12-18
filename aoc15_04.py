import utils
import hashlib

data = utils.get_input(2015, 4)[:-1]


def getHash(data, i):
    h = data + str(i)
    return hashlib.md5(h.encode('utf-8')).hexdigest()


i = 1
while True:
    hex_hash = getHash(data, i)
    if hex_hash[:5] == "00000":
        print(f"Part 1: {i}")
        break
    i += 1

while True:
    hex_hash = getHash(data, i)
    if hex_hash[:6] == "000000":
        print(f"Part 2: {i}")
        break
    i += 1
