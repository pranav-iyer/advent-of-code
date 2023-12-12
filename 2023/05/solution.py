import sys
from dataclasses import dataclass
from functools import cached_property


@dataclass
class MapRange:
    dest_start: int
    source_start: int
    length: int

    @property
    def source_end(self) -> int:
        return self.source_start + self.length - 1

    def is_in_source_range(self, num: int) -> bool:
        return num >= self.source_start and num - self.source_start < self.length

    def map_number(self, num: int) -> int:
        return self.dest_start + num - self.source_start


@dataclass
class Range:
    start: int
    length: int

    @property
    def end(self):
        return self.start + self.length - 1

    def __str__(self) -> str:
        return f"{self.start}-{self.end}"


@dataclass
class Map:
    ranges: list[MapRange]

    @cached_property
    def ordered_start_list(self) -> list[int]:
        return sorted([rng.source_start for rng in self.ranges])

    def map_number(self, source: int) -> int:
        for rng in self.ranges:
            if rng.is_in_source_range(source):
                return rng.map_number(source)
        return source

    def map_range(self, rng: Range) -> list[Range]:
        print(f"mapping rng {rng}")
        if rng.length == 0:
            return []

        for mrng in self.ranges:
            if mrng.is_in_source_range(rng.start):
                # we have found the mapping for the start of this range
                # if the whole range fits, party

                if mrng.is_in_source_range(rng.end):
                    return [Range(mrng.map_number(rng.start), rng.length)]
                else:
                    length_that_fits = mrng.source_end - rng.start + 1
                    current_range = Range(mrng.map_number(rng.start), length_that_fits)
                    rest_of_ranges = self.map_range(
                        Range(
                            rng.start + length_that_fits, rng.length - length_that_fits
                        )
                    )
                    return rest_of_ranges + [current_range]

        # this range maps to itself (at least to start..)

        start = min(s for s in self.ordered_start_list + [rng.end + 1] if s > rng.start)
        length_that_fits = start - rng.start

        if length_that_fits == rng.length:
            # entire range maps to itself
            return [Range(rng.start, rng.length)]
        else:
            current_range = Range(rng.start, length_that_fits)
            rest_of_ranges = self.map_range(
                Range(rng.start + length_that_fits, rng.length - length_that_fits)
            )
            return rest_of_ranges + [current_range]


def range_from_line(line: str) -> MapRange:
    parts = [int(x) for x in line.strip().split()]
    assert len(parts) == 3
    return MapRange(*parts)


def parse_input(input: str) -> tuple[list[int], list[Map]]:
    lines = [line.strip() for line in input.splitlines()]
    seeds = [int(x) for x in lines[0].split()[1:]]
    maps = []
    ranges = []
    for i in range(3, len(lines)):
        line = lines[i]
        if not line:
            continue
        if "map:" in line:
            maps.append(Map(ranges))
            ranges = []
        else:
            ranges.append(range_from_line(line))

    maps.append(Map(ranges))
    return seeds, maps


def part1(input: str):
    seeds, maps = parse_input(input)
    locations = []
    for seed in seeds:
        location = seed
        for map in maps:
            new_location = map.map_number(location)
            location = new_location
        locations.append(location)
    return min(locations)


def part2(input: str):
    seeds, maps = parse_input(input)
    ranges = []
    for i in range(0, len(seeds), 2):
        ranges.append(Range(seeds[i], seeds[i + 1]))
    for map in maps:
        new_ranges = []
        for rng in ranges:
            mapped_ranges = map.map_range(rng)
            new_ranges.extend(mapped_ranges)
        print(f"mapped {len(ranges)} ranges to {len(new_ranges)} new ranges.")
        ranges = new_ranges
    return min(rng.start for rng in ranges)


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
