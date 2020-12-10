import operator
import pathlib
from dataclasses import dataclass
from typing import Dict


def main():
    instructions = instruction_parser(pathlib.Path('puzzle_input.txt').read_text())
    acc = process(instructions)
    print(acc)


@dataclass
class Operation:
    instruction: str
    arg: int
    op: operator

    def __post_init__(self):
        self.arg = int(self.arg)

        if self.op == '-':
            self.op = operator.sub
        elif self.op == '+':
            self.op = operator.add


def instruction_parser(raw_instructions) -> Dict[int, Operation]:
    all_instructions = dict()
    step = 0
    for unparsed_instruction in raw_instructions.split('\n'):
        if unparsed_instruction.strip():
            instruction, argument = unparsed_instruction.split(" ")
            all_instructions[step] = Operation(
                instruction=instruction,
                arg=argument[1:],
                op=argument[:1]
            )
            step += 1
    return all_instructions


def process(instructions, accumulator=0):
    processed_steps = set()
    step = 0

    while True:
        operation = instructions[step]

        if step in processed_steps:
            return accumulator
        processed_steps.add(step)

        if operation.instruction == 'nop':
            step += 1
            continue
        elif operation.instruction == 'acc':
            accumulator = operation.op(accumulator, operation.arg)
            step += 1
        elif operation.instruction == 'jmp':
            step = operation.op(step, operation.arg)


if __name__ == '__main__':
    main()




