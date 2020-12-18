import pathlib


def main():
    instructions = instruction_parser(pathlib.Path('puzzle_input.txt').read_text())

    memory = {}
    for instruction_group in instructions:
        mask = instruction_group['mask']
        for instruction in instruction_group['subgroups']:
            binary_value = f"{instruction[1]:b}"
            memory[instruction[0]] = bitmask_filter(mask, binary_value)

    count = 0
    for v in memory.values():
        count += int(v, 2)

    print(count)


def bitmask_filter(mask, binary_value):
    result = ""
    for idx, val in enumerate(f"{binary_value:0>36}"):
        if mask[idx] == 'X':
            result += val
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
