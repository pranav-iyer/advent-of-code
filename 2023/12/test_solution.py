import pytest

from solution import (Record, Template, count_matches, matches,
                      possible_patterns, stars_bars)


def test_stars_bars():
    assert len(list(stars_bars(10, 4))) == 286


@pytest.mark.parametrize(
    ["template", "group_sizes", "count"],
    [
        ("???.###", [1, 1, 3], 1),
        (".??..??...?##.", [1, 1, 3], 4),
        ("?#?#?#?#?#?#?#?", [1, 3, 1, 6], 1),
        ("????.#...#...", [4, 1, 1], 1),
        ("????.######..#####.", [1, 6, 5], 4),
        ("?###????????", [3, 2, 1], 10),
    ],
)
def test_count_matches(template, group_sizes, count):
    assert count_matches(Template([c for c in template]), tuple(group_sizes)) == count


@pytest.mark.parametrize(
    ["line", "count"],
    [
        ("???.### 1,1,3", 1),
        (".??..??...?##. 1,1,3", 4),
        ("?#?#?#?#?#?#?#? 1,3,1,6", 1),
        ("????.#...#... 4,1,1", 1),
        ("????.######..#####. 1,6,5", 4),
        ("?###???????? 3,2,1", 10),
    ],
)
def test_count_matches_fived(line, count):
    record = Record.from_line(line)

    assert count_matches(record.template, tuple(record.group_sizes)) == count
