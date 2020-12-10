from textwrap import dedent

import pytest

from day_8.part_two import Program, instruction_parser

data = dedent("""
        nop +0
        acc +1
        jmp +4
        acc +3
        jmp -3
        acc -99
        acc +1
        jmp -4
        acc +6
        """)


@pytest.fixture
def broken_program():
    instructions = instruction_parser(data)
    return Program(instructions)


@pytest.fixture
def working_program():
    instructions = instruction_parser(data)
    instructions[7].instruction = 'nop'
    return Program(instructions)


def test_program_loops_infinitely(broken_program):
    assert broken_program.process() == (False, 5)


def test_program_finishes(working_program):
    assert working_program.process() == (True, 8)


if __name__ == '__main__':
    pytest.main()
