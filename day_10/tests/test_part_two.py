from day_10.part_two import calculate_all_paths


def test_small_dataset():
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
    assert calculate_all_paths(data) == 8


def test_large_dataset():
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

    data = [int(s) for s in data.split('\n') if s.strip()]
    assert calculate_all_paths(data) == 19208
