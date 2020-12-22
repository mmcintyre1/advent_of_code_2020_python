import itertools
import pathlib


def main():
    ticket_info = pathlib.Path('puzzle_input.txt').read_text()
    unparsed_seat_ranges, my_ticket, nearby_tickets = ticket_info.split('\n\n')
    seat_ranges = parse_seat_ranges(unparsed_seat_ranges)

    bad_tickets = []
    for nearby_ticket in nearby_tickets.split('\n')[1:]:
        invalid_fields = validator(nearby_ticket, seat_ranges)
        if invalid_fields:
            bad_tickets.append(invalid_fields)

    print(sum(itertools.chain(*bad_tickets)))


def parse_seat_ranges(unparsed_seat_ranges):
    seat_ranges = []
    for ticket_range in unparsed_seat_ranges.split('\n'):
        tmp_seat_ranges = ticket_range.split(': ')[-1]
        tmp = []
        for group in tmp_seat_ranges.split(' or '):
            mini, maxi = group.split('-')
            tmp.append(list(range(int(mini), int(maxi) + 1)))
        seat_ranges.append(list(itertools.chain(*tmp)))

    return seat_ranges


def validator(ticket, seat_ranges):
    invalid_fields = []
    for t in ticket.split(','):
        t = int(t)
        for group in seat_ranges:
            if any(x for x in group if x == t):
                break
        else:
            invalid_fields.append(t)

    return invalid_fields


if __name__ == '__main__':
    main()
