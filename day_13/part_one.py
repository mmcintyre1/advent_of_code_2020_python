import pathlib


def main():
    schedule = pathlib.Path('puzzle_input.txt').read_text()
    earliest_departure, available_buses = parse_schedule(schedule)
    print(get_closest_arrival(earliest_departure, available_buses))


def parse_schedule(unparsed_schedule):
    earliest_departure, available_buses = unparsed_schedule.split('\n')
    available_buses = [
        int(bus.strip())
        for bus in available_buses.split(',')
        if bus.strip() and bus != 'x'
    ]
    return int(earliest_departure.strip()), available_buses


def get_closest_number(number, target):
    return number * (target // number + 1)


def get_closest_arrival(earliest_departure, buses):
    closest_arrivals = {}
    for bus_id in buses:
        closest_arrivals[bus_id] = get_closest_number(bus_id, earliest_departure)

    closest = min(closest_arrivals.keys(), key=lambda k: closest_arrivals[k])

    return (closest_arrivals[closest] - earliest_departure) * closest


if __name__ == '__main__':
    main()
