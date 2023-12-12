import functools
import math
import sys
from collections import UserList
from collections.abc import Generator
from dataclasses import dataclass
from enum import Enum
from functools import wraps
from itertools import chain, combinations, repeat, zip_longest
from typing import Literal


class State(str, Enum):
    OPERATIONAL = "."
    DAMAGED = "#"
    UNKNOWN = "?"


class Template(UserList[State]):
    def __str__(self):
        return "".join(x for x in self)

    def __hash__(self):
        return hash(tuple(self))


class Guess(UserList[Literal[State.OPERATIONAL] | Literal[State.DAMAGED]]):
    def __str__(self):
        return "".join(x for x in self)


def matches(template: Template, guess: Guess):
    if len(template) != len(guess):
        raise RuntimeError(
            f"Template is not same length as guess: {len(template)}, {len(guess)}"
        )

    for t, g in zip(template, guess):
        if t == State.OPERATIONAL and g != State.OPERATIONAL:
            return False
        if t == State.DAMAGED and g != State.DAMAGED:
            return False

    return True


def stars_bars(
    n: int, k: int, disallowed_locations: set[int] | None = None
) -> Generator[list[int], None, None]:
    """Given n balls, and k distinguishable bins, generates all possible
    distributions of n into k. In the form of a generator of lists of length
    k indicating how many balls go into the k-th bin.
    """
    if not disallowed_locations:
        disallowed_locations = set()
    for bar_locs in combinations(range(n + k - 1), k - 1):
        if any(b in disallowed_locations for b in bar_locs):
            continue
        result = "".join("|" if x in bar_locs else "*" for x in range(n + k - 1))
        yield [len(x) for x in result.split("|")]


def possible_patterns(
    group_sizes: list[int], length: int, disallowed_locations: set[int] | None = None
) -> Generator[Guess, None, None]:
    n_groups = len(group_sizes)
    min_length = sum(group_sizes) + n_groups - 1
    extra_space = length - min_length
    print(extra_space, n_groups + 1)

    # we have n_groups + 1 spots to distribute our extra_space
    for space_sizes in stars_bars(extra_space, n_groups + 1, disallowed_locations):
        result: Guess = Guess()
        for space_length, group_length in zip_longest(space_sizes, group_sizes):
            result.extend([State.OPERATIONAL for _ in range(space_length)])
            if group_length:
                result.extend([State.DAMAGED for _ in range(group_length)])
                result.append(State.OPERATIONAL)
        yield result[:-1]  # get rid of last extra operational state


def debug(f):
    @wraps(f)
    def inner(*args):
        print(f.__name__, ",".join(str(a) for a in args))
        result = f(*args)
        print("return", f.__name__, ",".join(str(a) for a in args), "=>", result)
        return result

    return inner


@functools.cache
def count_matches(template: Template, group_sizes: tuple[int, ...]) -> int:
    # no groups, so all the rest should be operational
    if len(group_sizes) == 0:
        if State.DAMAGED in template:
            return 0
        else:
            return 1

    # we have some groups

    # check if all the groups are longer than template
    extra_space = len(template) - (sum(group_sizes) + len(group_sizes) - 1)
    if extra_space < 0:
        return 0

    # check if the entire template is unknown, then we can calculate
    if all(c == State.UNKNOWN for c in template):
        # stars bars with extra_space stars and len(group_sizes) + 1 bars
        if extra_space > 0:
            return math.comb(extra_space + len(group_sizes) + 1 - 1, extra_space)
        else:
            return 1

    if template[0] == State.OPERATIONAL:
        return count_matches(template[1:], group_sizes)
    elif template[0] == State.DAMAGED:
        if group_sizes[0] == 1:
            if len(template) == 1:
                return 1
            elif template[1] == State.OPERATIONAL or template[1] == State.UNKNOWN:
                return count_matches(template[2:], group_sizes[1:])
            else:
                return 0
        else:
            for i in range(group_sizes[0]):
                if i > len(template):
                    return 0
                if template[i] == State.OPERATIONAL:
                    return 0
            if group_sizes[0] == len(template):
                return 1
            elif template[group_sizes[0]] == State.DAMAGED:
                return 0
            else:
                return count_matches(template[group_sizes[0] + 1 :], group_sizes[1:])
    else:
        # unknown first element
        if group_sizes[0] == 1:
            if len(template) == 1:
                first_is_damaged = 1
            elif template[1] == State.OPERATIONAL or template[1] == State.UNKNOWN:
                first_is_damaged = count_matches(template[2:], group_sizes[1:])
            else:
                first_is_damaged = 0

            first_is_operational = count_matches(template[1:], group_sizes)
            return first_is_damaged + first_is_operational
        else:
            for i in range(group_sizes[0]):
                if i > len(template):
                    first_is_damaged = 0
                    break
                if template[i] == State.OPERATIONAL:
                    first_is_damaged = 0
                    break
            else:
                if group_sizes[0] == len(template):
                    first_is_damaged = 1
                elif template[group_sizes[0]] == State.DAMAGED:
                    first_is_damaged = 0
                else:
                    first_is_damaged = count_matches(
                        template[group_sizes[0] + 1 :], group_sizes[1:]
                    )

            first_is_operational = count_matches(template[1:], group_sizes)
            return first_is_damaged + first_is_operational


@dataclass
class Record:
    template: Template
    group_sizes: list[int]

    @property
    def damaged_locations(self):
        return {i for i, s in enumerate(self.template) if s == State.DAMAGED}

    @classmethod
    def from_line(cls, line: str):
        state_str, size_str = line.strip().split()
        template = Template([State(c) for c in state_str])
        group_sizes = [int(n) for n in size_str.split(",")]
        return cls(template, group_sizes)

    @classmethod
    def from_line_p2(cls, line: str):
        state_str, size_str = line.strip().split()
        state_str = "?".join([state_str for _ in range(5)])
        size_str = ",".join([size_str for _ in range(5)])
        template = Template([State(c) for c in state_str])
        group_sizes = [int(n) for n in size_str.split(",")]
        return cls(template, group_sizes)

    def __str__(self) -> str:
        return f"{''.join(self.template)} {','.join(str(n) for n in self.group_sizes)}"

    def arrangement_count(self) -> int:
        total = 0
        for p in possible_patterns(self.group_sizes, len(self.template)):
            if matches(self.template, p):
                total += 1
        return total

    def arrangement_count_p2(self) -> int:
        return count_matches(self.template, tuple(self.group_sizes))


def part1(input: str):
    records = [Record.from_line(line) for line in input.splitlines()]
    total = 0
    for i, r in enumerate(records):
        total += r.arrangement_count()
    return total


def part2(input: str):
    records = [Record.from_line_p2(line) for line in input.splitlines()]
    total = 0
    for i, r in enumerate(records):
        print("record", i, r)
        total += r.arrangement_count_p2()
    return total


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
