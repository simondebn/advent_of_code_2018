# ADVENT OF CODE 2018
# Day 3 : No Matter How You Slice It #

from collections import defaultdict
import re

input_file_path = './aoc_d3_inputs.txt'


def overlapping_claims(path):
    lines = open(input_file_path, 'r').readlines()
    claims = map(lambda s: map(int, re.findall(r'-?\d+', s)), lines)
    coord_inventory = defaultdict(list)
    overlaps = {}  # Part 2

    for (claim_number, start_x, start_y, width, height) in claims:
        overlaps[claim_number] = set()
        for i in range(start_x, start_x + width):
            for j in range(start_y, start_y + height):
                if coord_inventory[i, j]:
                    for number in coord_inventory[(i, j)]:  # P2
                        overlaps[number].add(claim_number)  # P2
                        overlaps[claim_number].add(number)  # P2
                coord_inventory[i, j].append(claim_number)

    res = 0
    for pt, claim_id in coord_inventory.items():
        # print(str(pt) + '::' + str(claim_id))
        if len(coord_inventory[pt]) > 1:
            res = res + 1

    for key, n in overlaps.items():  # P2
        if len(n) == 0:              # P2
            return res, key


print(overlapping_claims(input_file_path))
