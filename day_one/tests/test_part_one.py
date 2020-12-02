from day_one.part_one import product_of_2020


def test_part_one():
    data = [
        1721,
        979,
        366,
        299,
        675,
        1456,
    ]

    assert product_of_2020(data) == 514579
