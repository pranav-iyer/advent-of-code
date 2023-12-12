import sys

RACES = [(42, 308), (89, 1170), (91, 1291), (89, 1467)]

RACE2 = (42899189, 308117012911467)


def compute_distance(time_held: int, total_time: int) -> int:
    return (total_time - time_held) * time_held


def part1(input: str):
    total = 1
    for time, distance in RACES:
        times = [t for t in range(1, time) if compute_distance(t, time) > distance]
        total *= len(times)
    return total


def part2(input: str):
    time, distance = RACE2
    return len([t for t in range(1, time) if compute_distance(t, time) > distance])


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
