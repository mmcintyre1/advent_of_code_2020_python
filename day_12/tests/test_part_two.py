from textwrap import dedent

from day_12.part_two import Ship, parse_instructions


def test_small_instruction_set():
    unparsed_instructions = dedent("""
    F10
    N3
    F7
    R90
    F11""")

    inst = parse_instructions(unparsed_instructions)

    ship = Ship()
    for direction, spaces in inst:
        ship.move(direction, spaces)

    assert ship.get_manhattan_distance() == 286
