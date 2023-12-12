import math
import sys
from dataclasses import dataclass

DIRECTIONS = {"L": 0, "R": 1}


def parse_directions(line: str):
    return [DIRECTIONS[c] for c in line.strip()]


def parse_nodes(lines: list[str]):
    nodes: dict[str, tuple[str, str]] = {}
    for line in lines:
        line = line.strip()
        key, vals = [x.strip() for x in line.split("=")]
        left, right = [
            x.strip() for x in vals.replace("(", "").replace(")", "").split(",")
        ]

        nodes[key] = (left, right)
    return nodes


def part1(input: str):
    lines = input.splitlines()

    directions = parse_directions(lines[0])
    nodes = parse_nodes(lines[2:])

    steps = 0
    current = "AAA"
    while current != "ZZZ":
        direction = directions[steps % len(directions)]
        current = nodes[current][direction]
        steps += 1
    return steps


#
# def part2(input: str):
#     lines = input.splitlines()
#
#     directions = parse_directions(lines[0])
#     n_dirs = len(directions)
#     nodes = parse_nodes(lines[2:])
#
#     starting_nodes = ["BXA", "KBA", "VTA", "AAA", "HMA", "HLA"]
#     cycle_times = [0 for _ in starting_nodes]
#     for i, n in enumerate(starting_nodes):
#         curr = n
#         steps = 0
#         while True:
#             if steps > 0 and steps % n_dirs == 0 and curr == n:
#                 cycle_times[i] = steps
#                 print(n, steps)
#                 break
#             direction = directions[steps % n_dirs]
#             curr = nodes[curr][direction]
#             steps += 1
#     return cycle_times


@dataclass
class ZIndexInfo:
    indices: list[int]
    next_node: str


def part2(input: str):
    lines = input.splitlines()

    directions = parse_directions(lines[0])
    n_dirs = len(directions)
    nodes = parse_nodes(lines[2:])

    # pre-compute all of the numbers, for which, N steps after we will be on Z
    z_times: dict[str, ZIndexInfo] = {}
    for n in nodes:
        curr = n
        indices = []
        for step in range(n_dirs):
            if curr[2] == "Z":
                indices.append(step)
            curr = nodes[curr][directions[step]]

        z_times[n] = ZIndexInfo(indices, next_node=curr)

    new_nodes = {k: v.next_node for k, v in z_times.items()}

    starting_nodes = ["BXA", "KBA", "VTA", "AAA", "HMA", "HLA"]
    cycle_times = [0 for _ in starting_nodes]
    for i, n in enumerate(starting_nodes):
        steps = 0
        curr = n
        while curr[2] != "Z":
            curr = new_nodes[curr]
            steps += 1

        cycle_times[i] = steps

    return n_dirs * math.lcm(*cycle_times)


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
