from dataclasses import dataclass
from enum import auto, Enum

with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines() if line.strip()]


class Direction(Enum):
    NORTH = auto()
    WEST = auto()
    SOUTH = auto()
    EAST = auto()

    def left(self) -> "Direction":
        match self:
            case Direction.NORTH:
                return Direction.WEST
            case Direction.WEST:
                return Direction.SOUTH
            case Direction.SOUTH:
                return Direction.EAST
            case Direction.EAST:
                return Direction.NORTH


@dataclass
class Point:
    x: int
    y: int

    def __str__(self) -> str:
        return f"P({self.x},{self.y})"

    def __repr__(self) -> str:
        return f"P({self.x},{self.y})"

    def __getitem__(self, i):
        if i == 0:
            return self.x
        elif i == 1:
            return self.y
        else:
            raise IndexError("Point has only two coordinates")

    def dirto(self, nxt: "Point") -> Direction:
        if self.x != nxt.x and self.y != nxt.y:
            raise RuntimeError("Diagonal")
        if self.x == nxt.x:
            if self.y < nxt.y:
                return Direction.NORTH
            else:
                return Direction.SOUTH
        else:
            if self.x < nxt.x:
                return Direction.EAST
            else:
                return Direction.WEST


@dataclass
class Span:
    before: Direction
    after: Direction

    def encloses(self, dir: Direction) -> bool:
        clockwise = [Direction.SOUTH, Direction.WEST, Direction.NORTH, Direction.EAST]
        curr = clockwise.index(self.before)
        while curr != clockwise.index(self.after):
            if clockwise[curr] == dir:
                return True
            curr += 1
        if clockwise[curr] == dir:
            return True
        return False


def rectarea(p1: Point, p2: Point):
    return abs(p1.x - p2.x + 1) * abs(p1.y - p2.y + 1)


def part1():
    points = [Point(*(int(x) for x in line.split(","))) for line in lines]
    N = len(points)
    maxarea = -1
    for i in range(N):
        for j in range(i + 1, N):
            area = rectarea(points[i], points[j])
            if area > maxarea:
                maxarea = area
    return maxarea


def part2():
    points = [Point(*(int(x) for x in line.split(","))) for line in lines]
    N = len(points)

    # to the left is inside
    spans = [
        Span(points[i].dirto(points[(i - 1) % N]), points[i].dirto(points[(i + 1) % N]))
        for i in range(N)
    ]

    return N


print(part2())
