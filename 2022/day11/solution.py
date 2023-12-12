import sys
from collections.abc import Callable
from dataclasses import dataclass
from enum import Enum
from typing import Literal


class Operation(Enum):
    ADD = 1
    MULTIPLY = 2


FACTOR_LCM = 9699690


@dataclass
class Monkey:
    items: list[int]
    operation: Operation
    operand: int | Literal["old"]
    divisor: int
    true_monkey: int
    false_monkey: int
    inspection_count: int

    @classmethod
    def from_paragraph(cls, lines: list[str]):
        items = [
            int(x.strip()) for x in lines[0].strip().split(":")[1].strip().split(",")
        ]
        operation = (
            Operation.MULTIPLY
            if lines[1].strip().split("old")[1].split()[0] == "*"
            else Operation.ADD
        )
        try:
            operand = int(lines[1].strip().split("old", 1)[1].split()[1])
        except ValueError:
            operand = "old"

        divisor = int(lines[2].split("by")[1].strip())

        true_monkey = int(lines[3].split("monkey")[1].strip())
        false_monkey = int(lines[4].split("monkey")[1].strip())

        return cls(items, operation, operand, divisor, true_monkey, false_monkey, 0)

    def get_throws(self, relieve=True):
        throws = []
        for i in range(len(self.items)):
            # reduce size
            self.items[i] = self.items[i] % FACTOR_LCM

            self.inspection_count += 1

            # operate
            if self.operation == Operation.ADD:
                if isinstance(self.operand, int):
                    self.items[i] = self.items[i] + self.operand
                else:
                    self.items[i] = self.items[i] + self.items[i]
            else:
                if isinstance(self.operand, int):
                    self.items[i] = self.items[i] * self.operand
                else:
                    self.items[i] = self.items[i] * self.items[i]

            # relieve
            if relieve:
                self.items[i] = self.items[i] // 3

            # throw?
            if self.items[i] % self.divisor == 0:
                throws.append((self.true_monkey, self.items[i]))
            else:
                throws.append((self.false_monkey, self.items[i]))

        self.items = []
        return throws


@dataclass
class MonkeyCircle:
    monkeys: list[Monkey]

    def run_round(self, relieve=True):
        for monkey in self.monkeys:
            throws = monkey.get_throws(relieve)
            for i, val in throws:
                self.monkeys[i].items.append(val)


def part1(input: str):
    lines = [line.strip() for line in input.splitlines()]

    monkeys = []
    for i in range(0, len(lines), 7):
        monkeys.append(Monkey.from_paragraph(lines[i + 1 : i + 7]))

    circle = MonkeyCircle(monkeys)

    for _ in range(20):
        circle.run_round()

    counts = sorted([m.inspection_count for m in circle.monkeys])

    return counts[-1] * counts[-2]


def part2(input: str):
    lines = [line.strip() for line in input.splitlines()]

    monkeys = []
    for i in range(0, len(lines), 7):
        monkeys.append(Monkey.from_paragraph(lines[i + 1 : i + 7]))

    circle = MonkeyCircle(monkeys)

    for i in range(10_000):
        print("round", i)
        circle.run_round(relieve=False)

    counts = sorted([m.inspection_count for m in circle.monkeys])

    return counts[-1] * counts[-2]


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
