import pathlib
import math
from typing import List


def main():
    slope_pattern = [
        x.strip()
        for x in pathlib.Path("puzzle_input.txt").read_text().split('\n')
        if x.strip()
    ]

    all_trees = math.prod([
        tree_counter(slope_pattern, down=x, right=y)
        for x, y in
        [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]
    ])
    print(all_trees)


def enumerate2(xs, start=0, step=1):
    for x in xs:
        yield start, x
        start += step


def tree_counter(slope_pattern: List[str], down: int = 1, right: int = 1) -> int:
    tree_count = 0
    sliced_pattern = slope_pattern[::down]
    for idx, row in enumerate2(sliced_pattern, step=right):
        if row[idx % len(row)] == '#':
            tree_count += 1
    return tree_count


if __name__ == '__main__':
    main()
