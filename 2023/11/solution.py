import copy
import sys


def get_grid(input: str):
    return [[c for c in line if not c.isspace()] for line in input.splitlines()]


def expand_grid(grid: list[list[str]]) -> list[list[str]]:
    N = len(grid)
    M = len(grid[0])
    new_grid = copy.deepcopy(grid)

    # expand colums
    cols_to_insert = []
    for j in range(M):
        if all(new_grid[i][j] == "." for i in range(N)):
            cols_to_insert.append(j)

    for col in reversed(cols_to_insert):
        for i in range(N):
            new_grid[i].insert(col, ".")

    N = len(new_grid)
    M = len(new_grid[0])

    # expand rows
    rows_to_insert = []
    for i in range(N):
        if all(c == "." for c in grid[i]):
            rows_to_insert.append(i)

    for row in reversed(rows_to_insert):
        new_grid.insert(row, ["." for _ in range(M)])

    return new_grid


def galaxy_distance(g1: tuple[int, int], g2: tuple[int, int]):
    return abs(g1[0] - g2[0]) + abs(g1[1] - g2[1])


def get_empty_rows(grid: list[list[str]]):
    empty_rows = []
    for i in range(len(grid)):
        if all(c == "." for c in grid[i]):
            empty_rows.append(i)
    return empty_rows


def get_empty_cols(grid: list[list[str]]):
    empty_cols = []
    for j in range(len(grid[0])):
        if all(grid[i][j] == "." for i in range(len(grid))):
            empty_cols.append(j)
    return empty_cols


def get_count_between(lst: list[int], a: int, b: int):
    if a < b:
        low = a
        high = b
    else:
        low = b
        high = a

    return len([x for x in lst if x > low and x < high])


def part1(input: str):
    grid = get_grid(input)
    grid = expand_grid(grid)

    N = len(grid)
    M = len(grid[0])

    coords: list[tuple[int, int]] = []
    for i in range(N):
        for j in range(M):
            if grid[i][j] == "#":
                coords.append((i, j))

    total_distance = 0
    for i in range(len(coords)):
        for j in range(i):
            total_distance += galaxy_distance(coords[i], coords[j])

    return total_distance


def part2(input: str):
    grid = get_grid(input)

    N = len(grid)
    M = len(grid[0])

    coords: list[tuple[int, int]] = []
    for i in range(N):
        for j in range(M):
            if grid[i][j] == "#":
                coords.append((i, j))

    empty_rows = get_empty_rows(grid)
    empty_cols = get_empty_cols(grid)

    total_distance = 0
    for i in range(len(coords)):
        for j in range(i):
            total_distance += (
                galaxy_distance(coords[i], coords[j])
                + get_count_between(empty_rows, coords[i][0], coords[j][0]) * 999_999
                + get_count_between(empty_cols, coords[i][1], coords[j][1]) * 999_999
            )

    return total_distance


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
