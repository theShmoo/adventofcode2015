import utils
import re

double_re = re.compile(r"(.)\1")
vowels_re = re.compile(r"[aeiou]")
bad_re = re.compile(r"(ab|cd|pq|xy)")

data = utils.get_input(2015, 5).split("\n")

matches = []

for d in data:
    vowel_matches = re.findall(vowels_re, d)
    if len(vowel_matches) < 3:
        continue

    if re.search(bad_re, d):
        continue

    if not re.search(double_re, d):
        continue

    matches.append(d)

print(f"Part 1: Found {len(matches)}")

matches = []

rule1_re = re.compile(r"(..).*\1")
rule2_re = re.compile(r"(.).\1")
for d in data:
    if not re.search(rule2_re, d):
        continue
    else:
        print(f"{d} is ok for rule 2")

    if not re.search(rule1_re, d):
        continue
    else:
        print(f"{d} is ok for rule 1")

    matches.append(d)

print(f"Part 2: Found {len(matches)}")
