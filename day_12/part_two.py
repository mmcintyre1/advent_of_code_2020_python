import operator
import pathlib
from dataclasses import dataclass
from enum import Enum


def main():
    inst = parse_instructions(pathlib.Path('puzzle_input.txt').read_text())

    ship = Ship()
    for direction, spaces in inst:
        ship.move(direction, spaces)
        print(ship.coordinates)
        print(ship.waypoint)

    print(ship.get_manhattan_distance())


def parse_instructions(unparsed_instructions):
    return [
        (line[:1], int(line[1:]))
        for line in unparsed_instructions.split('\n')
        if line.strip()
    ]


class Compass(Enum):
    """We use Enum instead of a dataclass here
    because Compass is immutable"""
    North = (0, 1)
    South = (0, -1)
    East = (1, 0)
    West = (-1, 0)


@dataclass
class Coordinates:
    def __init__(self, x: int = 0, y: int = 0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"


class Ship:
    rotations = {
        90: 1,
        180: 2,
        270: 3,
        0: 4
    }

    directions = {
        'N': Compass.North,
        'E': Compass.East,
        'S': Compass.South,
        'W': Compass.West
    }

    def __init__(self):
        self.waypoint = Coordinates(10, 1)
        self.coordinates = Coordinates()

    def __turn(self, direction: str, degrees: int):
        if direction == 'L':
            degrees = 360 - degrees
        degrees = degrees % 360
        for _ in range(self.rotations[degrees]):
            self.waypoint.x, self.waypoint.y = self.waypoint.y, -self.waypoint.x

    def __move_waypoint(self, direction: str, spaces: int):
        for _ in range(spaces):
            self.waypoint.x += self.directions[direction].value[0]
            self.waypoint.y += self.directions[direction].value[1]

    def __move_ship(self, spaces: int):
        for _ in range(spaces):
            self.coordinates.x += self.waypoint.x
            self.coordinates.y += self.waypoint.y

    def move(self, direction: str, spaces: int):
        if direction in ('L', 'R'):
            self.__turn(direction, spaces)
        elif direction == 'F':
            self.__move_ship(spaces)
        elif direction in ('N', 'E', 'S', 'W'):
            self.__move_waypoint(direction, spaces)
        else:
            raise ValueError(f"{direction} not an allowed field.")

    def get_manhattan_distance(self):
        return abs(self.coordinates.x) + abs(self.coordinates.y)


if __name__ == '__main__':
    main()
