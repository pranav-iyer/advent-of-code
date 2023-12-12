import sys
from dataclasses import dataclass


@dataclass
class Scorecard:
    magic_numbers: set[str]
    my_numbers: list[str]

    @property
    def matching_numbers(self):
        return len([n for n in self.my_numbers if n in self.magic_numbers])


def parse_scorecard(line: str) -> Scorecard:
    line = line.strip()
    content = line.split(":")[1]
    magic_numbers = set(x.strip() for x in content.split("|")[0].split() if x.strip())
    my_numbers = list(x.strip() for x in content.split("|")[1].split() if x.strip())
    return Scorecard(magic_numbers, my_numbers)


def part1(input: str):
    total_score = 0
    for line in input.splitlines():
        line = line.strip()
        content = line.split(":")[1]
        magic_numbers = set(
            x.strip() for x in content.split("|")[0].split() if x.strip()
        )
        my_numbers = list(x.strip() for x in content.split("|")[1].split() if x.strip())
        matching_numbers = [n for n in my_numbers if n in magic_numbers]
        if matching_numbers:
            score = 2 ** (len(matching_numbers) - 1)
            total_score += score
    return total_score


def part2(input: str):
    scorecards = [parse_scorecard(line) for line in input.splitlines()]
    N = len(scorecards)
    num_copies = [1 for _ in range(N)]
    for i in range(N):
        for j in range(1, scorecards[i].matching_numbers + 1):
            if i + j < N:
                num_copies[i + j] += num_copies[i]
    return sum(num_copies)


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
