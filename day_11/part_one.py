import pathlib
from dataclasses import dataclass, field
from itertools import product
from textwrap import dedent
from typing import Dict, Tuple, Union

floor = object()

seat_lookup = {
    "#": False,
    "L": True
}


def main():
    seat_data = pathlib.Path('puzzle_input.txt').read_text()
    plane = plane_parser(seat_data)
    while not plane.boarded:
        plane.board_plane()
        print(plane)
    print(plane.get_occupied_seats())


@dataclass
class Seat:
    is_empty: bool


class Plane:
    all_adjacent_paths = [x for x in product(range(-1, 2), repeat=2) if x != (0, 0)]
    boarded = False

    def __init__(self):
        self.seats: Union[Dict[Tuple[int, int], Seat], floor] = dict()

    def is_adjacent_occupied(self, x, y, max_adjacent=4):
        current_adjacent = 0
        for path in self.all_adjacent_paths:
            try:
                adjacent_seat = self.seats[x + path[0], y + path[1]]
            except KeyError:
                pass
            else:
                if adjacent_seat is not floor and not adjacent_seat.is_empty:
                    current_adjacent += 1
        return current_adjacent >= max_adjacent

    def board_plane(self):
        boarded_seats = {}
        for coords, seat in self.seats.items():
            if seat is floor:
                boarded_seats[coords] = floor
            else:
                if seat.is_empty and not self.is_adjacent_occupied(x=coords[0], y=coords[1], max_adjacent=1):
                    boarded_seats[coords] = Seat(is_empty=False)
                elif not seat.is_empty and self.is_adjacent_occupied(x=coords[0], y=coords[1]):
                    boarded_seats[coords] = Seat(is_empty=True)
                else:
                    boarded_seats[coords] = seat

        if boarded_seats == self.seats:
            self.boarded = True

        self.seats = boarded_seats

    def get_grid_size(self):
        return max(self.seats.keys())

    def get_occupied_seats(self):
        return sum([
            1
            for seat in self.seats.values()
            if seat is not floor and not seat.is_empty
        ])

    def __str__(self):
        empty_char = "L"
        occupied_char = "#"
        floor_char = "."

        grid_rows, grid_cols = self.get_grid_size()
        grid = ""

        for x in range(grid_rows+1):
            for y in range(grid_cols+1):
                seat = self.seats[x, y]
                if seat is floor:
                    grid += floor_char
                elif seat.is_empty:
                    grid += empty_char
                else:
                    grid += occupied_char
            grid += '\n'
        return grid


def plane_parser(seat_data) -> Plane:
    plane = Plane()
    for row_idx, row in enumerate(seat_data.split('\n')):
        for col_idx, seat in enumerate(row):
            if seat == '.':
                plane.seats[(row_idx, col_idx)] = floor
            else:
                plane.seats[(row_idx, col_idx)] = Seat(is_empty=seat_lookup[seat])

    return plane


if __name__ == '__main__':
    main()
