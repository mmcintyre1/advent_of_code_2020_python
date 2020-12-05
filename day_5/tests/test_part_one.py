import pytest

from day_5.part_one import get_seat_id


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ('BFFFBBFRRR', 567),
        ('FFFBBBFRRR', 119),
        ('BBFFBBFRLL', 820)
    ]
)
def test_get_seat_ids(test_input, expected):
    assert get_seat_id(test_input) == expected
