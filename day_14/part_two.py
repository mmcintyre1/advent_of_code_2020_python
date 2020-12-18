import pathlib
from collections import defaultdict
from itertools import combinations, permutations, product


def main():
    instructions = instruction_parser(pathlib.Path('puzzle_input.txt').read_text())
    memory = run(instructions)
    print(count_memory(memory))


def run(instructions):
    memory = {}
    for instruction_group in instructions:
        mask = instruction_group['mask']
        for memory_address, _ in instruction_group['subgroups']:
            binary_value = f"{memory_address:b}"
            memory[memory_address] = bitmask_filter(mask, binary_value)

    return memory


def count_memory(memory):
    count = 0
    for memory_register in memory.values():
        local_registers = []
        if 'X' in memory_register:
            print(memory_register)
            # all_replacements = product([0, 1], memory_register.count('X'))
            # print(list(all_replacements))
        # count += int(memory_register, 2)

    return count


def bitmask_filter(mask, binary_value):
    result = ""
    for idx, val in enumerate(f"{binary_value:0>36}"):
        if mask[idx] == 'X':
            result += 'X'
        else:
            result += mask[idx]

    return f"{result:0>36}"


def instruction_parser(raw_instructions):
    all_groupings = []
    group = None
    for s in raw_instructions.split('\n'):
        if s.startswith('mask'):
            if group:
                all_groupings.append(group)
            group = {"mask": s.split("= ")[-1], "subgroups": []}
        else:
            memory, value = s.split(" = ")
            memory_location = memory.partition("[")[-1].partition("]")[0]
            group["subgroups"].append((int(memory_location), int(value)))

    all_groupings.append(group)

    return all_groupings


if __name__ == '__main__':
    main()
