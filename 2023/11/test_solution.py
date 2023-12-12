from solution import expand_grid


def test_grid_expansion():
    grid = [
        [".", ".", "#"],
        [".", ".", "."],
        ["#", ".", "#"],
    ]

    assert expand_grid(grid) == [
        [".", ".", ".", "#"],
        [".", ".", ".", "."],
        [".", ".", ".", "."],
        ["#", ".", ".", "#"],
    ]
