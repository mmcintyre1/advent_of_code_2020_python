from textwrap import dedent

from day_9.part_one import encoding_check


def parse_sequence(data):
    return [
        int(x.strip())
        for x in data.split('\n')
        if x.strip()
    ]


def test_checks_valid_encoding():
    unparsed_nums = dedent("""
    35
    20
    15
    25
    47
    40
    62
    55
    65
    95
    102
    117
    150
    182
    127
    219
    299
    277
    309
    576
    """)
    seq = parse_sequence(unparsed_nums)

    assert encoding_check(seq, preamble=5) == 127
