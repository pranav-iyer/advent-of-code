import functools

with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines() if line.strip()]

adj = {line.split(":")[0]: line.split(":")[1].strip().split(" ") for line in lines}
adj["out"] = []


@functools.cache
def count_paths(start: str) -> int:
    if start == "out":
        return 1
    total = 0
    for nxt in adj[start]:
        total += count_paths(nxt)
    return total


@functools.cache
def count_paths_to(start: str, end: str) -> int:
    if start == end:
        return 1
    total = 0
    for nxt in adj[start]:
        total += count_paths_to(nxt, end)
    return total


def part1():
    return count_paths("you")


def part2():
    dac_fft = (
        count_paths_to("svr", "dac")
        * count_paths_to("dac", "fft")
        * count_paths_to("fft", "out")
    )
    fft_dac = (
        count_paths_to("svr", "fft")
        * count_paths_to("fft", "dac")
        * count_paths_to("dac", "out")
    )
    return dac_fft + fft_dac


print(part2())
