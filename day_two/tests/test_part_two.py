from textwrap import dedent

from day_two.part_two import parse_password


def test_password_valid_count():
    all_passwords = dedent("""
    1-3 a: abcde
    1-3 b: cdefg
    2-9 c: ccccccccc
    """)

    parsed_passwords = [
        parse_password(p)
        for p in all_passwords.split('\n')
        if p
    ]

    valid_count = sum([
        1 for p in parsed_passwords if p.is_valid
    ])

    assert valid_count == 1

