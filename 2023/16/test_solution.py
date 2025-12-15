import pytest
from solution import Board, Direction, next_dirs


@pytest.mark.parametrize(
    ["indir", "char", "outdirs"],
    [
        ("LEFT", "|", {"UP", "DOWN"}),
        ("RIGHT", "|", {"UP", "DOWN"}),
        ("UP", "|", {"UP"}),
        ("RIGHT", "\\", {"DOWN"}),
    ],
)
def test_next_dirs(indir, char, outdirs):
    assert set(next_dirs(Direction[indir], char)) == {Direction[d] for d in outdirs}


@pytest.mark.parametrize(
    ["input", "n"],
    [
        (
            """
            ...
            ...
            ...
            """,
            3,
        ),
        (
            r"""
            ..\
            ...
            ...
            """,
            5,
        ),
        (
            r"""
            .\.
            .-.
            ...
            """,
            5,
        ),
        (
            r"""
            .\.
            .-\
            ...
            """,
            6,
        ),
        (
            r"""
            .|...\....
            |.-.\.....
            .....|-...
            ........|.
            ..........
            .........\
            ..../.\\..
            .-.-/..|..
            .|....-|.\
            ..//.|....
            """,
            46,
        ),
    ],
)
def test_trace_path(input, n):
    board = Board.from_input(input)
    board.trace_path((0, 0), Direction.RIGHT)
    assert board.count_illuminated() == n
