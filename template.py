import sys


def part1(input: str):
    return "Not implemented"


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
