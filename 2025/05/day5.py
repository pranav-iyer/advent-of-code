with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

sep_idx = lines.index("")
ranges = [tuple(int(x) for x in row.split("-")) for row in lines[:sep_idx]]
ids = [int(x) for x in lines[sep_idx + 1 :]]


def in_range(val: int, rng: tuple[int, int]) -> bool:
    return val >= rng[0] and val <= rng[1]


def in_any_range(val: int) -> bool:
    return any(in_range(val, rng) for rng in ranges)


print(len(list(filter(in_any_range, ids))))


def consolidate_ranges(ranges: list[tuple[int, int]]) -> list[tuple[int, int]]:
    ranges.sort()
    i = 0
    while i < len(ranges) - 1:
        if ranges[i][1] >= ranges[i + 1][0]:
            # next range starts in this one, we can group them
            if ranges[i + 1][1] > ranges[i][1]:
                ranges[i] = (ranges[i][0], ranges[i + 1][1])
            ranges.pop(i + 1)
        else:
            i += 1

    return ranges


print(sum(rng[1] - rng[0] + 1 for rng in consolidate_ranges(ranges)))
