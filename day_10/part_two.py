import pathlib


def main():
    # data = [
    #     int(s)
    #     for s in pathlib.Path('puzzle_input.txt').read_text().split('\n')
    #     if s.strip()
    # ]
    data = [1, 2, 3, 4]
    print(calculate_all_paths(data))


def calculate_all_paths(data):
    last = max(data)
    # need to append 1 to start to account for 0 as starting point
    accumulation_array = [1] + [0 for _ in range(last)]
    for r in sorted(data):
        accumulation_array[r] = accumulation_array[r-1] + accumulation_array[r-2] + accumulation_array[r-3]
        if r == last:
            return accumulation_array[r]


if __name__ == '__main__':
    main()