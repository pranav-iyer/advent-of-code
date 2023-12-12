import sys
from enum import Enum

import matplotlib.pyplot as plt
import numpy as np

CYCLES = [19, 59, 99, 139, 179, 219]


class InstructionType(Enum):
    ADDX = 1
    NOOP = 2


def parse_instruction(line: str) -> tuple[InstructionType, int | None]:
    parts = [p.strip() for p in line.split() if p.strip]
    match parts[0]:
        case "noop":
            return (InstructionType.NOOP, None)
        case "addx":
            return (InstructionType.ADDX, int(parts[1]))
        case _:
            raise ValueError(f"Bad instruction type {line}")


def part1(input: str):
    X: int = 1
    X_history = [1]

    instructions = [parse_instruction(line) for line in input.splitlines()]

    for instype, val in instructions:
        if instype == InstructionType.NOOP:
            X_history.append(X)
        else:
            X_history.append(X)
            X += val
            X_history.append(X)

    return sum((j + 1) * X_history[j] for j in CYCLES)


W = 40
H = 6


def render(screen, inscount: int, X: int):
    render = ((inscount // 40) % 6, inscount % 40)
    if abs(X - (inscount % 40)) <= 1:
        screen[render] = 1
    else:
        screen[render] = 0


def part2(input: str):
    X: int = 1
    inscount = 0

    instructions = [parse_instruction(line) for line in input.splitlines()]

    screen = np.zeros((6, 40))
    for instype, val in instructions:
        # CRT renders
        render(screen, inscount, X)
        inscount += 1
        if instype == InstructionType.NOOP:
            pass
        else:
            # CRT renders
            render(screen, inscount, X)
            inscount += 1

            # addx finishes
            X += val

    plt.imshow(screen)
    plt.show()


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
