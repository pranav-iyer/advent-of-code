from solution import part1, part2


def test_weird_boy():
    input = """
    ........
    F----7..
    LSF7.|..
    .||L7|..
    .LJ.LJ..
    ........
    """
    assert part2(input) == 1
