import copy
import operator
import pathlib
from dataclasses import dataclass
from typing import Dict


def main():
    instructions = instruction_parser(pathlib.Path('puzzle_input.txt').read_text())
    mixed_instructions = instruction_mixer(instructions)

    for instruction_set in mixed_instructions:
        p = Program(instruction_set)
        is_complete, value = p.process()
        if is_complete:
            print(value)
            break


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


class Program:
    def __init__(self, instructions, accumulator=0):
        self.accumulator = accumulator
        self.processed_steps = set()
        self.step = 0
        self.last_step = len(instructions)
        self.instructions = instructions

    def process(self):
        while True:
            operation = self.instructions[self.step]
            if self.step in self.processed_steps:
                return False, self.accumulator
            self.processed_steps.add(self.step)
            self._process_handler(operation)
            if self.step == self.last_step:
                return True, self.accumulator

    def _process_handler(self, operation):
        if operation.instruction == 'nop':
            self.step += 1
            return
        elif operation.instruction == 'acc':
            self.accumulator = operation.op(self.accumulator, operation.arg)
            self.step += 1
        elif operation.instruction == 'jmp':
            self.step = operation.op(self.step, operation.arg)


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


def instruction_mixer(instructions):
    mixed_instructions = []
    for idx, (step, instruction) in enumerate(instructions.items()):
        if instruction.instruction == 'nop':
            d_copy = copy.deepcopy(instructions)
            d_copy[step].instruction = 'jmp'
            mixed_instructions.append(d_copy)
        elif instruction.instruction == 'jmp':
            d_copy = copy.deepcopy(instructions)
            d_copy[step].instruction = 'nop'
            mixed_instructions.append(d_copy)

    return mixed_instructions


if __name__ == '__main__':
    main()
