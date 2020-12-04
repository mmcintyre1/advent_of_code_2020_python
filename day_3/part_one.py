import pathlib
from typing import List


def main():
    slope_pattern = [
        x.strip()
        for x in pathlib.Path("puzzle_input.txt").read_text().split('\n')
        if x.strip()
    ]

    print(tree_counter(slope_pattern))


def enumerate2(xs, start=0, step=1):
    for x in xs:
        yield start, x
        start += step


def tree_counter(slope_pattern: List[str]) -> int:
    tree_count = 0
    for idx, row in enumerate2(slope_pattern, step=3):
        if row[idx % len(row)] == '#':
            tree_count += 1
    return tree_count


if __name__ == '__main__':
    main()

