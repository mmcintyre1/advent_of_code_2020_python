from textwrap import dedent

from day_13.part_one import get_closest_arrival, parse_schedule


def test_bus_schedule():
    schedule = dedent("""
    939
    7,13,x,x,59,x,31,19
    """).strip()
    earliest_departure, available_buses = parse_schedule(schedule)
    assert get_closest_arrival(earliest_departure, available_buses) == 295
