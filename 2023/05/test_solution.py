import pytest
from solution import Map, range_from_line

TEST_MAP = """
50 98 2
52 50 48
"""


@pytest.mark.parametrize(
    ["input", "output"],
    [
        (0, 0),
        (49, 49),
        (50, 52),
        (51, 53),
        (97, 99),
        (98, 50),
        (99, 51),
        (100, 100),
    ],
)
def test_map_number(input, output):
    map = Map([range_from_line(line) for line in TEST_MAP.splitlines() if line.strip()])
    assert map.map_number(input) == output


TEST_MAP_2 = """
0 15 37
37 52 2
39 0 15
"""


def second_test():
    map = Map(
        [range_from_line(line) for line in TEST_MAP_2.splitlines() if line.strip()]
    )
    assert map.map_number(14) == 14
