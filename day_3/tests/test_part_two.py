from textwrap import dedent

import pytest

from day_3.part_two import tree_counter


def test_tree_counter_path_right_one_down_one():
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

    assert tree_counter(slope_pattern, right=1, down=1) == 2


def test_tree_counter_path_right_three_down_one():
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

    assert tree_counter(slope_pattern, right=3, down=1) == 7


def test_tree_counter_path_right_five_down_one():
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

    assert tree_counter(slope_pattern, right=5, down=1) == 3


def test_tree_counter_path_right_seven_down_one():
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

    assert tree_counter(slope_pattern, right=7, down=1) == 4


# @pytest.mark.skip()
def test_tree_counter_path_right_one_down_two():
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

    assert tree_counter(slope_pattern, right=1, down=2) == 2


if __name__ == '__main__':
    pytest.main()