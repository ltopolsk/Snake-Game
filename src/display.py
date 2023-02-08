import curses
from src.board import Board
# import time
# from curses import textpad


def main(stdscr):
    
    board1 = Board("board1")
    board1.load_from_file("plansza1.txt")
    curses.curs_set(0)

    width = board1.get_width()
    height = board1.get_height()
    snake = [(height//2, width//2 + 1), (height//2, width//2), (height//2, width//2 - 1)]
    for i in range(len(board1.table)):
        stdscr.addstr(i, 0, board1.get_line(i))
    for x, y in snake:
        stdscr.addstr(x, y, "S") 
    stdscr.refresh()
    stdscr.getch()
    direction = curses.KEY_UP

    while 1:
        key = stdscr.getch()

        if key in [curses.KEY_UP, curses.KEY_DOWN, curses.KEY_RIGHT, curses.KEY_LEFT]:
            direction = key

        head = snake[0]

        if direction == curses.KEY_UP:
            new_head = ((head[0] - 1) % height, head[1])
        elif direction == curses.KEY_LEFT:
            new_head = (head[0], (head[1] - 1) % width)
        elif direction == curses.KEY_RIGHT:
            new_head = (head[0], (head[1] + 1) % width)
        elif direction == curses.KEY_DOWN:
            new_head = ((head[0] + 1) % height, head[1])

        snake.insert(0, new_head)
        stdscr.addstr(new_head[0], new_head[1], "S")
        stdscr.addstr(snake[-1][0], snake[-1][1], " ")
        snake.pop()
        stdscr.refresh()


curses.wrapper(main)