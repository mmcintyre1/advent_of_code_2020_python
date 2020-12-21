def main():
    nums = [0, 14, 6, 20, 1, 4]
    print(speak_n_say(nums, 2020))


def speak_iter(sequence):
    # preload the cache
    memo = {
        k: count
        for count, k in enumerate(sequence[:-1], start=1)
    }

    num = sequence[-1]
    idx = len(sequence)

    while True:
        last_idx = memo.get(num, 0)
        memo[num] = idx
        if last_idx == 0:
            num = 0
        else:
            num = idx - last_idx
        idx += 1
        yield idx, num


def speak_n_say(sequence, end_number):
    for idx, num in speak_iter(sequence):

        if idx == end_number:
            return num


if __name__ == '__main__':
    main()
