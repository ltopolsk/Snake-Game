import curses
from src.board import Board


class Snake():
    """
    This class repesents snake as a list of coordinates. Every coordinate is a tuple of two numbers.
    :type coordinates: list (of tuples)
    First coordinate in list is snake's head, last one is snake's tail
    """

    def __init__(self, row0, column0, row1, column1, row2, column2):
        """initializes snake"""
        self.coordinates = [(row0, column0), (row1, column1), (row2, column2)]

    def set_direction(self, key, direction):
        """
        Sets direction. If key is not one of steering key, returns previous direction
        """
        if key in {curses.KEY_RIGHT, curses.KEY_UP, curses.KEY_DOWN, curses.KEY_LEFT}:
            return key
        return direction

    def move(self, direction):
        """
        Adds coordinate of head after snake's move to snake's coordinates
        """
        moves = {
            curses.KEY_LEFT: (0, -1),
            curses.KEY_RIGHT: (0, 1),
            curses.KEY_UP: (-1, 0),
            curses.KEY_DOWN: (1, 0)
        }
        head = self.coordinates[0]
        new_head = ((head[0] + moves[direction][0]) % Board.HEIGHT, (head[1] + moves[direction][1]) % Board.WIDTH)
        self.coordinates.insert(0, new_head)

    def len(self):
        """Returns snake's length"""
        return len(self.coordinates)

    def is_alive(self, barriers):
        """Checks if snake is alive."""
        if self.coordinates[0] in barriers or self.coordinates[0] in self.coordinates[1:]:
            return False
        return True
