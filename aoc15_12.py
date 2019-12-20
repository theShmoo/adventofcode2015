import utils
import json


def flatten(x, ints, include_red=True):
    if type(x) is dict:
        if include_red:
            for v in x.values():
                flatten(v, ints, include_red)
        elif all(type(v) is not str or "red" not in v for v in x.values()):
            for v in x.values():
                flatten(v, ints, include_red)
    elif type(x) is list:
        for a in x:
            flatten(a, ints, include_red)
    elif type(x) is int:
        ints.append(x)


data = json.loads(utils.get_input(2015, 12))
ints = []
flatten(data, ints)
print(f"Part 1 : sum {sum(ints)}")

ints = []
flatten(data, ints, False)
print(f"Part 2 : sum {sum(ints)}")
