from collections import defaultdict

with open("input.txt") as f:
    raw_input = f.read()

INPUT = [list(line.strip()) for line in raw_input.splitlines()]


def is_symbol(c: str):
    return not c.isspace() and not c.isdigit() and c != "."


def is_asterisk(c: str):
    return c == "*"


def get_adjacent_indices(i: int) -> tuple[int | None, int | None, int | None]:
    if i == 0:
        return (None, 0, 1)
    elif i == len(INPUT) - 1:
        return (i - 1, i, None)
    else:
        return (i - 1, i, i + 1)


def is_part_number(input: list[list[str]], i: int, j: int, length: int) -> bool:
    """
    Checks if the number starting at location (i,j) is adjacent
    to a symbol, i.e. a part number
    """
    # check left
    if j != 0:
        if any(is_symbol(input[k][j - 1]) for k in get_adjacent_indices(i) if k):
            return True

    # check top and bottom
    for x in range(length):
        if any(is_symbol(input[k][j + x]) for k in get_adjacent_indices(i) if k):
            return True

    # check right
    if j + length <= len(input[0]) - 1:
        if any(is_symbol(input[k][j + length]) for k in get_adjacent_indices(i) if k):
            return True

    return False


def get_adjacent_stars(
    input: list[list[str]], i: int, j: int, length: int
) -> list[tuple[int, int]]:
    """
    Returns the indices of all stars adjacent to this number
    """
    stars = []
    # check left
    if j != 0:
        for k in get_adjacent_indices(i):
            if k and input[k][j - 1] == "*":
                stars.append((k, j - 1))

    # check top and bottom
    for x in range(length):
        for k in get_adjacent_indices(i):
            if k and input[k][j + x] == "*":
                stars.append((k, j + x))

    # check right
    if j + length <= len(input[0]) - 1:
        for k in get_adjacent_indices(i):
            if k and input[k][j + length] == "*":
                stars.append((k, j + length))

    return stars


def part1():
    sum = 0
    i = 0
    while i < len(INPUT):
        j = 0
        while j < len(INPUT[0]):
            # check for number
            if INPUT[i][j].isdigit():
                length = 1
                while j + length < len(INPUT[0]) and INPUT[i][j + length].isdigit():
                    length += 1
                if is_part_number(INPUT, i, j, length):
                    sum += int("".join(INPUT[i][j : j + length]))

                j += length
            else:
                j += 1
        i += 1
    return sum


def part2():
    results = defaultdict(list)
    i = 0
    while i < len(INPUT):
        j = 0
        while j < len(INPUT[0]):
            # check for number
            if INPUT[i][j].isdigit():
                length = 1
                while j + length < len(INPUT[0]) and INPUT[i][j + length].isdigit():
                    length += 1

                number = int("".join(INPUT[i][j : j + length]))
                for star in get_adjacent_stars(INPUT, i, j, length):
                    results[star].append(number)

                j += length
            else:
                j += 1
        i += 1

    # sum gear ratios
    sum = 0
    for star in results:
        if len(results[star]) == 2:
            sum += results[star][0] * results[star][1]

    return sum


if __name__ == "__main__":
    print(part2())
