import pathlib


def main():
    all_boarding_passes = [
        x.strip()
        for x in pathlib.Path("puzzle_input.txt").read_text().split('\n')
        if x.strip()
    ]

    max_seat_id = max([
        get_seat_id(bp)
        for bp in all_boarding_passes
        ])
    print(max_seat_id)


def binary_reducer(sequence, lower_bound='F', upper_bound='B'):
    current_range = list(range(0, 2 ** len(sequence)))
    for instruction in sequence:
        half = len(current_range) // 2
        if instruction == upper_bound:
            current_range = current_range[half:]
        elif instruction == lower_bound:
            current_range = current_range[:half]
        else:
            break

    return current_range


def get_row(sequence):
    return binary_reducer(sequence)[0]


def get_column(sequence):
    return binary_reducer(sequence, lower_bound='L', upper_bound='R')[0]


def get_seat_id(sequence):
    row_id = get_row(sequence[:7])
    column_id = get_column(sequence[7:])
    return row_id * 8 + column_id


if __name__ == '__main__':
    main()