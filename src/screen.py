import curses
from src.board import Board


class Screen():
    """
    This class initializes a window (using curses), in which the game takes place, in terminal.
    :type: board = Board
    """

    def __init__(self, board):
        """initializes the window"""
        self.stdscr = curses.initscr()
        self.board = board

    def start_window(self):
        """
        Changes settings of the window:
        - allows to use special keys (such as right arrow)
        - makes cursor dissapear
        - makes possible not to wait for input key
        """
        curses.noecho()
        curses.cbreak()
        self.stdscr.keypad(True)
        curses.curs_set(0)
        self.stdscr.nodelay(1)
        self.stdscr.timeout(100)

    def end_window(self):
        """
        Changes back the settings of the window after pressing any key
        """
        self.stdscr.nodelay(0)
        self.stdscr.getch()
        curses.echo()
        curses.nocbreak()
        self.stdscr.keypad(False)
        curses.endwin()

    def show_board(self):
        """shows board on the window"""
        for row in range(Board.HEIGHT):
            for column in range(Board.WIDTH):
                self.add_char(row, column, self.board.table[row][column])

    def add_char(self, row, column, char):
        """adds any char in place deifned by row and column on the window"""
        self.stdscr.addstr(row, column, char)
