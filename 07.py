from typing import Literal, NewType

Board = NewType('Board', list[list[Literal[' ', 'X', 'O']]])


def init() -> Board:
    return Board([
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' '],
    ])


def check_win(board: Board) -> bool:
    return False


def play(board: Board) -> None:
    pass


play([[' ', ' ']])
