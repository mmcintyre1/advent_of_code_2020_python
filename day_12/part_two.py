import operator
import pathlib
from dataclasses import dataclass
from enum import Enum


def main():
    inst = parse_instructions(pathlib.Path('puzzle_input.txt').read_text())

    ship = Ship()
    for direction, spaces in inst:
        ship.move(direction, spaces)

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


class Ship:
    degree_lookup = {
        0: 'E',
        90: 'S',
        180: 'W',
        270: 'N'
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
        self.facing = 0

    def __turn(self, direction: str, degrees: int):
        if direction == 'L':
            op = operator.sub
        elif direction == 'R':
            op = operator.add
        else:
            raise ValueError(f'{direction} not valid.')
        self.facing = op(self.facing, degrees) % 360

    def __move_waypoint(self):
        pass

    def __move_ship(self):
        pass

    def move(self, direction, spaces):
        pass


    # def move(self, direction: str, spaces: int):
    #     if direction in ('L', 'R'):
    #         self.turn(direction, spaces)
    #         return
    #     if direction == 'F':
    #         direction = self.degree_lookup[self.facing]
    #     elif direction == 'B':
    #         direction = self.degree_lookup[self.facing] % 180
    #
    #     direction = self.directions[direction]
    #
    #     for _ in range(spaces):
    #         self.coordinates.x += direction.value[0]
    #         self.coordinates.y += direction.value[1]

    def get_manhattan_distance(self):
        return abs(self.coordinates.x) + abs(self.coordinates.y)


if __name__ == '__main__':
    main()
