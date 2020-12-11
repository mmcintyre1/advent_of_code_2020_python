import itertools
import pathlib
from collections import deque
from typing import List


def main():
    sequence = [
        int(x.strip())
        for x in pathlib.Path('puzzle_input.txt').read_text().split('\n')
        if x.strip()
    ]
    encoding_check(sequence)


def encoding_check(sequence: List[int], preamble: int = 25):
    queue = deque(sequence[:preamble], maxlen=preamble)
    for num in sequence[preamble:]:
        all_combos = itertools.permutations(queue, 2)
        if any((match := x[0] + x[1]) == num for x in all_combos):
            print(f'{match} is valid')
        else:
            print(f'{num} is not valid. Exiting sequence')
            return num
        queue.append(num)


if __name__ == '__main__':
    main()
