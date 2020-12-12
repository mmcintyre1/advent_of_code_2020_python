import pathlib
from collections import Counter


def main():
    adapters = sorted([
        int(x)
        for x in pathlib.Path('puzzle_input.txt').read_text().split('\n')
        if x.strip()
    ])

    joltages = get_joltage_diffs(adapters)
    print(joltages[1] * joltages[3])


def get_joltage_diffs(adapters):
    # need to make sure the input is sorted
    # need to set first and last socket
    adapters.insert(0, 0)
    adapters.append(max(adapters) + 3)

    return Counter([
        (x - adapters[idx-1])
        for idx, x in enumerate(adapters)
        if idx > 0
    ])


if __name__ == '__main__':
    main()
