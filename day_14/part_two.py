import pathlib
from itertools import product
from typing import Dict


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
            filtered_value = bitmask_filter(mask, binary_value)
            all_memory_addresses = resolve_floating_registers(filtered_value)
            memory.update(all_memory_addresses)

    return memory


def count_memory(memory):
    count = 0
    for memory_register in memory.values():
        count += int(memory_register, 2)

    return count


def bitmask_filter(mask: str, binary_value: str):
    result = ""
    for idx, val in enumerate(f"{binary_value:0>36}"):
        if mask[idx] == 'X':
            result += 'X'
        elif mask[idx] == '1':
            result += mask[idx]
        else:
            result += val

    return f"{result:0>36}"


def resolve_floating_registers(memory_register: str) -> Dict[int, str]:
    memory_update = {}
    floating_indices = [idx for idx, _ in enumerate(memory_register) if _ == 'X']
    for float_group in product('01', repeat=memory_register.count('X')):
        tmp_memory = list(memory_register)
        for float_index, replacement in zip(floating_indices, float_group):
            tmp_memory[float_index] = replacement
        memory_update[int("".join(tmp_memory), 2)] = "".join(tmp_memory)

    return memory_update


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
