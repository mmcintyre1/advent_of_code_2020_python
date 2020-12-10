from textwrap import dedent

from day_8.part_one import instruction_parser, process


def test_instructions():
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

    assert process(instruction_parser(data)) == 5
