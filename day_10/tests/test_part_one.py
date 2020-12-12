from day_10.part_one import get_joltage_diffs


def test_small_sequence():
    data = """
        16
        10
        15
        5
        1
        11
        7
        19
        6
        12
        4
        """

    data = sorted([int(s) for s in data.split('\n') if s.strip()])
    joltage_diffs = get_joltage_diffs(data)
    assert joltage_diffs[1] == 7
    assert joltage_diffs[3] == 5


def test_larger_sequence():
    data = """
    28
    33
    18
    42
    31
    14
    46
    20
    48
    47
    24
    23
    49
    45
    19
    38
    39
    11
    1
    32
    25
    35
    8
    17
    7
    9
    4
    2
    34
    10
    3
    """

    data = sorted([int(s) for s in data.split('\n') if s.strip()])
    joltage_diffs = get_joltage_diffs(data)
    assert joltage_diffs[1] == 22
    assert joltage_diffs[3] == 10
