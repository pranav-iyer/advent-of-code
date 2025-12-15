import sys
from collections import deque
from enum import Enum
from typing import NamedTuple

Position = tuple[int, int]


class Direction(Enum):
    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4

    def dir_tuple(self):
        match self:
            case Direction.UP:
                return (-1, 0)
            case Direction.RIGHT:
                return (0, 1)
            case Direction.DOWN:
                return (1, 0)
            case Direction.LEFT:
                return (0, -1)

    def available_directions(self, must_turn: bool) -> list["Direction"]:
        match self:
            case Direction.UP | Direction.DOWN:
                dirs = [Direction.RIGHT, Direction.LEFT]
                if not must_turn:
                    dirs += [self]
                return dirs
            case Direction.RIGHT | Direction.LEFT:
                dirs = [Direction.UP, Direction.DOWN]
                if not must_turn:
                    dirs += [self]
                return dirs


class Key(NamedTuple):
    pos: Position
    dir: Direction
    steps_remaining: int


def eadd(pos: Position, dir: Direction) -> Position:
    dirtup = dir.dir_tuple()
    return (pos[0] + dirtup[0], pos[1] + dirtup[1])


class Grid(list[list[int]]):
    @classmethod
    def from_input(cls, input: str):
        return cls(
            [int(c) for c in line.strip()]
            for line in input.splitlines()
            if line.strip()
        )

    @property
    def N(self):
        return len(self)

    @property
    def M(self):
        return len(self[0])

    def at(self, pos: Position) -> int:
        return self[pos[0]][pos[1]]


def part1(input: str):
    grid = Grid.from_input(input)

    distances: dict[Key, int] = {}
    distances[Key((0, 0), Direction.RIGHT, 3)] = 0
    to_visit: deque[Key] = deque()
    to_visit.append(Key((0, 0), Direction.RIGHT, 3))

    while True:
        try:
            currpos, currdir, steps_remaining = to_visit.popleft()
        except IndexError:
            break

        print(currpos, currdir, steps_remaining)

        nextdirs = currdir.available_directions(steps_remaining <= 0)
        for d in nextdirs:
            # check if feasible
            nextpos = eadd(currpos, d)
            if nextpos[0] in range(0, grid.N) and nextpos[1] in range(0, grid.M):
                if d == currdir:
                    key = Key(nextpos, d, steps_remaining - 1)
                else:
                    key = Key(nextpos, d, 2)

                dist_thru_curr = distances[
                    Key(currpos, currdir, steps_remaining)
                ] + grid.at(nextpos)
                if key in distances:
                    # check if shorter than existing distance
                    if dist_thru_curr < distances[key]:
                        distances[key] = dist_thru_curr
                        to_visit.append(key)

                else:
                    distances[key] = dist_thru_curr
                    to_visit.append(key)

    return 0


def part2(input: str):
    return "Not implemented"


if __name__ == "__main__":
    if "2" not in sys.argv:
        with open("input.txt") as f:
            input1 = f.read()
        print("Part 1".center(80, "="))
        print("Solution:", part1(input1))

    if "1" not in sys.argv:
        with open("input.txt") as f:
            input2 = f.read()
        print("Part 2".center(80, "="))
        print("Solution:", part2(input2))
