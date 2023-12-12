import sys
from dataclasses import dataclass


@dataclass
class Pattern:
    numbers: list[int]

    def get_diff(self) -> "Pattern":
        diffs = []
        for i in range(1, len(self.numbers)):
            diffs.append(self.numbers[i] - self.numbers[i - 1])
        return Pattern(diffs)

    def is_zeros(self) -> bool:
        return all(x == 0 for x in self.numbers)

    @classmethod
    def from_line(cls, line: str):
        return cls([int(x) for x in line.split()])

    def __str__(self):
        return " ".join(str(x) for x in self.numbers)


class Pyramid:
    def __init__(self, root: Pattern):
        self.patterns = [root]
        current = root
        while not current.is_zeros():
            current = current.get_diff()
            self.patterns.append(current)

    def __str__(self):
        return "\n".join(str(patt) for patt in self.patterns)

    def next_value(self) -> int:
        prev = 0
        for patt in reversed(self.patterns):
            prev = patt.numbers[-1] + prev
        return prev

    def prev_value(self) -> int:
        prev = 0
        for patt in reversed(self.patterns):
            prev = patt.numbers[0] - prev
        return prev


def part1(input: str):
    lines = input.splitlines()
    sum = 0
    for line in lines:
        sum += Pyramid(Pattern.from_line(line)).next_value()
    return sum


def part2(input: str):
    lines = input.splitlines()
    sum = 0
    for line in lines:
        sum += Pyramid(Pattern.from_line(line)).prev_value()
    return sum


if __name__ == "__main__":
    try:
        part = int(sys.argv[1])
    except (IndexError, ValueError):
        part = 0

    match part:
        case part if part != 2:
            with open("input.txt", "r") as f:
                input1 = f.read()
            print("Part 1".center(80, "="))
            print(part1(input1))

        case part if part != 1:
            with open("input.txt", "r") as f:
                input2 = f.read()
            print("Part 2".center(80, "="))
            print(part2(input2))
