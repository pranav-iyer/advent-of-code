import sys
from collections import deque
from dataclasses import dataclass
from enum import Enum


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


Position = tuple[int, int]


def next_dirs(direction: Direction, curr_char: str) -> list[Direction]:
    match curr_char:
        case "|":
            if direction in (Direction.RIGHT, Direction.LEFT):
                return [Direction.UP, Direction.DOWN]
            return [direction]
        case "-":
            if direction in (Direction.UP, Direction.DOWN):
                return [Direction.LEFT, Direction.RIGHT]
            return [direction]
        case "/":
            if direction == Direction.UP:
                return [Direction.RIGHT]
            elif direction == Direction.RIGHT:
                return [Direction.UP]
            elif direction == Direction.LEFT:
                return [Direction.DOWN]
            elif direction == Direction.DOWN:
                return [Direction.LEFT]
            else:
                raise ValueError("Unreachable, invalid direction")

        case "\\":
            if direction == Direction.UP:
                return [Direction.LEFT]
            elif direction == Direction.LEFT:
                return [Direction.UP]
            elif direction == Direction.RIGHT:
                return [Direction.DOWN]
            elif direction == Direction.DOWN:
                return [Direction.RIGHT]
            else:
                raise ValueError("Unreachable, invalid direction")

        case ".":
            return [direction]

        case _:
            raise ValueError("Unreachable, should not trigger")


def eadd(pos: Position, direction: Direction) -> Position:
    dir_tuple = direction.dir_tuple()
    return (pos[0] + dir_tuple[0], pos[1] + dir_tuple[1])


class Board:
    def __init__(self, states: list[list[str]]):
        self.states = states
        self.illuminated_map = [[False for _ in row] for row in states]

    @property
    def N(self):
        return len(self.states)

    @property
    def M(self):
        return len(self.states[0])

    @classmethod
    def from_input(cls, input: str):
        states: list[list[str]] = []
        for line in input.splitlines():
            line = line.strip()
            if line:
                states.append([c for c in line])

        return cls(states)

    def illuminate(self, pos: Position) -> bool:
        already_illuminated = self.illuminated_map[pos[0]][pos[1]]
        if not already_illuminated:
            self.illuminated_map[pos[0]][pos[1]] = True
        return already_illuminated

    def reset(self):
        self.illuminated_map = [[False for _ in row] for row in self.states]

    def count_illuminated(self) -> int:
        return sum(sum(1 for i in row if i) for row in self.illuminated_map)

    # def trace_path(self, start: Position, direction: Direction):
    #     print("trace", start, direction)
    #     self.illuminate(*start)
    #     curr = eadd(start, direction)
    #     while (
    #         curr[0] in range(self.N)
    #         and curr[1] in range(self.N)
    #         and self.states[curr[0]][curr[1]] == "."
    #     ):
    #         self.illuminate(*curr)
    #         curr = eadd(curr, direction)
    #
    #     if curr[0] not in range(self.N) or curr[1] not in range(self.M):
    #         return
    #     self.illuminate(*curr)
    #
    #     # switch based on char
    #     dirs = next_dirs(direction, self.states[curr[0]][curr[1]])
    #     if len(dirs) == 1:
    #         self.trace_path(curr, dirs[0])
    #
    #     else:
    #         self.trace_path(curr, dirs[0])
    #         self.trace_path(curr, dirs[1])

    def trace_path(self, start: Position, direction: Direction):
        visited: set[tuple[Position, Direction]] = set()
        to_visit: deque[tuple[Position, Direction]] = deque()
        to_visit.append((start, direction))
        time = 1
        while True:
            try:
                currpos, currdir = to_visit.popleft()
            except IndexError:
                return
            visited.add((currpos, currdir))
            if not self.illuminate(currpos):
                time = 1
            else:
                time += 1
            nextdirs = next_dirs(currdir, self.states[currpos[0]][currpos[1]])
            for nextdir in nextdirs:
                nextpos = eadd(currpos, nextdir)
                if (
                    (nextpos, nextdir) not in visited
                    and nextpos[0] in range(self.N)
                    and nextpos[1] in range(self.M)
                ):
                    to_visit.append((nextpos, nextdir))


def part1(input: str):
    board = Board.from_input(input)
    board.trace_path((0, 0), Direction.RIGHT)
    return board.count_illuminated()


def part2(input: str):
    board = Board.from_input(input)
    max_ill = 0

    # down from top
    for j in range(board.M):
        board.trace_path((0, j), Direction.DOWN)
        curr_ill = board.count_illuminated()
        if curr_ill > max_ill:
            max_ill = curr_ill
        board.reset()

    # up from bottom
    for j in range(board.M):
        board.trace_path((board.N - 1, j), Direction.UP)
        curr_ill = board.count_illuminated()
        if curr_ill > max_ill:
            max_ill = curr_ill
        board.reset()

    # right form left
    for i in range(board.N):
        board.trace_path((i, 0), Direction.RIGHT)
        curr_ill = board.count_illuminated()
        if curr_ill > max_ill:
            max_ill = curr_ill
        board.reset()

    # left from right
    for i in range(board.N):
        board.trace_path((i, board.M - 1), Direction.LEFT)
        curr_ill = board.count_illuminated()
        if curr_ill > max_ill:
            max_ill = curr_ill
        board.reset()

    return max_ill


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
