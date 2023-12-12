import re

with open("input.txt") as f:
    input = f.read()

LIMITS = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


def parse_pull(pull: str):
    result = {}
    for match in re.finditer(r"(\d+) (\w+)", pull):
        result[match.group(2)] = int(match.group(1))
    return result


def is_pull_possible(pull: dict):
    return all(
        pull.get(color, 0) <= LIMITS[color] for color in ("red", "green", "blue")
    )


def get_min_cubes(pulls: list[dict]):
    return {
        color: max(pull.get(color, 0) for pull in pulls)
        for color in ("red", "green", "blue")
    }


def part1():
    matching_ids = []
    for line in input.splitlines():
        game_title, contents = line.split(":")

        game_id = int(game_title.strip()[5:])
        pulls = contents.split(";")
        if all(is_pull_possible(parse_pull(pull)) for pull in pulls):
            matching_ids.append(game_id)

    print(matching_ids)
    print(sum(matching_ids))


def part2():
    result = 0
    for line in input.splitlines():
        game_title, contents = line.split(":")
        game_id = int(game_title.strip()[5:])
        pulls = [parse_pull(pull) for pull in contents.split(";")]
        min_cubes = get_min_cubes(pulls)
        result += min_cubes["red"] * min_cubes["green"] * min_cubes["blue"]

    print(result)


if __name__ == "__main__":
    part2()
