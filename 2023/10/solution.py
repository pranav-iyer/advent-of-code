import sys

"""

Directions are labeled like this:


        (-1, 0)
(0, -1)         (0, 1)
        (1, 0)


"""

CHARS = {
    "|": {(-1, 0), (1, 0)},
    "-": {(0, -1), (0, 1)},
    "7": {(0, -1), (1, 0)},
    "J": {(-1, 0), (0, -1)},
    "L": {(-1, 0), (0, 1)},
    "F": {(1, 0), (0, 1)},
}


def get_grid(input: str) -> list[list[str]]:
    return [[c for c in line.strip()] for line in input.splitlines() if line.strip()]


def get_next_direction(c: str, last_direction: tuple[int, int]) -> tuple[int, int]:
    valid_dirs = CHARS.get(c)
    if not valid_dirs:
        raise ValueError(f"Ended up a dot from last_direction {last_direction}")

    if last_direction in valid_dirs:
        new_dir = valid_dirs.difference({last_direction}).pop()
        return new_dir

    raise ValueError(
        f"Direction {last_direction} not found in valid {valid_dirs} for char {c}"
    )


def eadd(t1: tuple[int, int], t2: tuple[int, int]):
    return (t1[0] + t2[0], t1[1] + t2[1])


def negate(t: tuple[int, int]):
    return (-t[0], -t[1])


def part1(input: str):
    grid = get_grid(input)
    N = len(grid)
    M = len(grid[0])
    start_pos = (0, 0)
    for i in range(N):
        for j in range(M):
            if grid[i][j] == "S":
                start_pos = (i, j)
                break

    start_direction = (1, 0)

    last_direction = negate(start_direction)
    curr = eadd(start_pos, start_direction)
    steps = 1
    while curr != start_pos:
        new_direction = get_next_direction(grid[curr[0]][curr[1]], last_direction)
        curr = eadd(curr, new_direction)
        last_direction = negate(new_direction)
        steps += 1
    return steps / 2


def part2(input: str):
    grid = get_grid(input)
    N = len(grid)
    M = len(grid[0])
    start_pos = (0, 0)
    for i in range(N):
        for j in range(M):
            if grid[i][j] == "S":
                start_pos = (i, j)
                break

    start_direction = (1, 0)
    last_direction = negate(start_direction)
    curr = eadd(start_pos, start_direction)
    path = {start_pos, curr}
    while curr != start_pos:
        new_direction = get_next_direction(grid[curr[0]][curr[1]], last_direction)
        curr = eadd(curr, new_direction)
        path.add(curr)
        last_direction = negate(new_direction)

    num_inside = 0
    for i in range(N):
        for j in range(M):
            if (i, j) in path:
                continue

            counter = 0
            last_dir = 0
            for k in range(j):
                if (i, k) in path:
                    match grid[i][k]:
                        case "|":
                            counter += 1
                        case "F":
                            last_dir = 1
                        case "L":
                            last_dir = -1
                        case "J":
                            if last_dir == 1:
                                counter += 1
                            elif last_dir == -1:
                                counter += 2
                        case "7" | "S":
                            if last_dir == 1:
                                counter += 2
                            elif last_dir == -1:
                                counter += 1

            if counter % 2 == 1:
                num_inside += 1

    return num_inside


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
            print("Solution:", part1(input1))

        case part if part != 1:
            with open("input.txt", "r") as f:
                input2 = f.read()
            print("Part 2".center(80, "="))
            print("Solution:", part2(input2))
