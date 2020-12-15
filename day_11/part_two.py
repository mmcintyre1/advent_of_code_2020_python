import pathlib
from dataclasses import dataclass
from itertools import product
from textwrap import dedent
from typing import Dict, Tuple, Union

floor = object()

seat_lookup = {
    "#": False,
    "L": True
}


def main():
    # seat_data = pathlib.Path('puzzle_input.txt').read_text()
    seat_data = dedent("""
    L.LL.LL.LL
    LLLLLLL.LL
    L.L.L..L..
    LLLL.LL.LL
    L.LL.LL.LL
    L.LLLLL.LL
    ..L.L.....
    LLLLLLLLLL
    L.LLLLLL.L
    L.LLLLL.LL
    """).strip()
    plane = plane_parser(seat_data)
    while not plane.boarded:
        plane.board_plane(max_adjacent=5)
        print(plane)
    print(plane.get_occupied_seats())


@dataclass
class Seat:
    is_empty: bool


class GridMovement:
    def __init__(self):
        self.x = 0
        self.y = 0

    def right(self):
        self.x += 1

    def left(self):
        self.x -= 1

    def up(self):
        self.y -= 1

    def down(self):
        self.y += 1

    def up_right(self):
        self.up()
        self.right()

    def down_right(self):
        self.down()
        self.right()

    def down_left(self):
        self.down()
        self.left()

    def up_left(self):
        self.up()
        self.left()

    def reset(self):
        self.x = 0
        self.y = 0

    def __str__(self):
        return f"({self.x}, {self.y})"


class Plane:
    boarded = False
    gm = GridMovement()

    def __init__(self):
        self.seats: Union[Dict[Tuple[int, int], Seat], floor] = dict()

    def is_adjacent_occupied(self, x, y, max_adjacent):
        current_adjacent = 0
        for move in (
            self.gm.right, self.gm.left, self.gm.up, self.gm.down, self.gm.down_left, self.gm.down_right,
            self.gm.up_right,self.gm.up_left
        ):
            self.gm.x, self.gm.y = x, y
            move()
            while True:
                try:
                    adjacent_seat = self.seats[self.gm.x, self.gm.y]
                except KeyError:
                    break
                if adjacent_seat is floor:
                    move()
                elif adjacent_seat.is_empty:
                    break
                else:
                    current_adjacent += 1
                    break
        return current_adjacent >= max_adjacent

    def board_plane(self, max_adjacent):
        boarded_seats = {}
        for coords, seat in self.seats.items():
            if seat is floor:
                boarded_seats[coords] = floor
            else:
                if seat.is_empty and not self.is_adjacent_occupied(x=coords[0], y=coords[1], max_adjacent=max_adjacent):
                    boarded_seats[coords] = Seat(is_empty=False)
                elif not seat.is_empty and self.is_adjacent_occupied(x=coords[0], y=coords[1], max_adjacent=max_adjacent):
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

        for y in range(grid_rows + 1):
            for x in range(grid_cols + 1):
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
    for y, row in enumerate(seat_data.split('\n')):
        for x, seat in enumerate(row):
            if seat == '.':
                plane.seats[(x, y)] = floor
            else:
                plane.seats[(x, y)] = Seat(is_empty=seat_lookup[seat])

    return plane


if __name__ == '__main__':
    main()
