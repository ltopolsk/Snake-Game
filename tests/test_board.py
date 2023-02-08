from src.board import Board, InvalidBoardException
import os
import pytest

board1 = Board()
board1.load_from_file(os.path.join("boards", "Example.txt"))
board2 = Board()
board2.load_from_file(os.path.join("boards", "WrongBoard1.txt"))
board3 = Board()
board3.load_from_file(os.path.join("boards", "Wrong Board2.txt"))
board4 = Board()
board4.load_from_file(os.path.join("boards", "Wrong Board3.txt"))
board5 = Board()
board5.load_from_file(os.path.join("boards", "Wrong Board4.txt"))


def test_load_board():
    assert board1.table[0][0] == Board.BARRIER_CHAR
    assert board1.table[1][0] == " "


def test_empty_places():
    assert board1.empty_places()[0] == (0, 12)


def test_barriers():
    assert board1.barriers()[0] == (0, 0)


def test_add_snake():
    snake_coordinates = [[1, 1], [1, 2], [1, 3]]
    board1.add_snake(snake_coordinates)
    assert board1.table[1][2] == Board.SNAKE_CHAR


def test_add_char():
    board1.add_char((1, 0), Board.FOOD_CHAR)
    assert board1.table[1][0] == Board.FOOD_CHAR


def test_invalid_board():
    with pytest.raises(OSError):
        board = Board()
        board.load_from_file("plansza3.txt")
    with pytest.raises(InvalidBoardException):
        board2.check_board()
        board3.check_board()
        board4.check_board()
