from day_1.part_two import product_of_2020


def test_part_two():
    data = [
        1721,
        979,
        366,
        299,
        675,
        1456,
    ]

    assert product_of_2020(data, n=3) == 241861950
