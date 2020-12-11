import pathlib
from typing import List


def main():
    sequence = [
        int(x.strip())
        for x in pathlib.Path('puzzle_input.txt').read_text().split('\n')
        if x.strip()
    ]
    print(encryption_breaker(sequence, magic_number=1639024365))


def encryption_breaker(nums: List[int], magic_number: int) -> int:
    for position in range(len(nums)):
        local_total = 0
        for idx, num in enumerate(nums[position:]):
            local_total += num
            if local_total == magic_number:
                matching_slice = nums[position:position + idx]
                return min(matching_slice) + max(matching_slice)
            elif local_total > magic_number:
                break
    return -1


if __name__ == '__main__':
    main()
