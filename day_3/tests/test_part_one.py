from textwrap import dedent

from day_3.part_one import tree_counter


def test_tree_counter():
    data = dedent("""
    ..##.......
    #...#...#..
    .#....#..#.
    ..#.#...#.#
    .#...##..#.
    ..#.##.....
    .#.#.#....#
    .#........#
    #.##...#...
    #...##....#
    .#..#...#.#
    """)

    slope_pattern = [
        x.strip()
        for x in data.split('\n')
        if x.strip()
    ]

    assert tree_counter(slope_pattern) == 7
