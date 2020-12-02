from itertools import permutations
import math
import pathlib
from typing import List


def product_of_2020(num_group: List[int], n: int = 2) -> int:
    all_groupings = permutations(num_group, n)
    for group in all_groupings:
        if sum(group) == 2020:
            return math.prod(group)


if __name__ == '__main__':
    puzzle_input = [int(x) for x in pathlib.Path("puzzle_input.txt").read_text().split()]
    print(product_of_2020(puzzle_input, n=3))
