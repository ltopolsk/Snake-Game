from src.snake import Snake
import pytest
from src.board import Board
import curses

board1 = Board()
board1.load_from_file("Example.txt")
snake = Snake(0, 3, 1, 3, 1, 2)
snake2 = Snake(0, 3, 1, 3, 1, 2)
snake1 = Snake(1, 24, 1, 23, 1, 22)
direction = curses.KEY_RIGHT


def test_is_alive():
    assert not snake.is_alive(board1.barriers())


def test_set_direction():
    new_direction = snake.set_direction(curses.KEY_UP, direction)
    assert new_direction == curses.KEY_UP


def test_len():
    assert snake.len() == 3


def test_move():
    snake.move(direction)
    snake1.move(direction)
    snake2.move(curses.KEY_UP)
    assert snake.coordinates[0] == (0, 4)
    assert snake1.coordinates[0] == (1, 0)
    assert snake2.coordinates[0] == (9, 3)
