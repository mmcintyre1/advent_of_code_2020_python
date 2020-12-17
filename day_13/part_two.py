import pathlib


def main():
    schedule = pathlib.Path('puzzle_input.txt').read_text().split('\n')[-1]
    print(get_time_steps(schedule))


def get_time_steps(schedule):
    buses = {
        int(bus_id): -idx % int(bus_id)
        for idx, bus_id in enumerate(schedule.split(","))
        if bus_id.strip() and bus_id != 'x'
    }

    iterator, step = 0, 1
    for bus in buses.keys():
        while iterator % bus != buses[bus]:
            iterator += step
        step *= bus

    return iterator


if __name__ == '__main__':
    main()
