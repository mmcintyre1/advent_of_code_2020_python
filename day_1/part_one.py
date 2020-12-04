from itertools import permutations
import pathlib
from typing import List


def product_of_2020(num_group: List[int]) -> int:
    all_groupings = permutations(num_group, 2)
    for first_num, second_num in all_groupings:
        if first_num + second_num == 2020:
            return first_num * second_num


if __name__ == '__main__':
    puzzle_input = [int(x) for x in pathlib.Path("puzzle_input.txt").read_text().split()]
    print(product_of_2020(puzzle_input))
