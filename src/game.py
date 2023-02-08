from src.snake import Snake
from src.board import Board
import curses
from src.screen import Screen
import time
from re import match


class InvalidArgumentsExpection(Exception):
    pass


class Game():
    """
    The snake game.
    :type: board_path = str
    :type: speed = str (any positive float number)
    :type: prob = str (any float number in range (0, 1> )
    :type: game_mode = str ("special" or "normal")
    :type: counter = int (counts how long lasts special mode)
    :type: board = Board
    :type: snake = Snake
    :type: window = Screen
    """
    def __init__(self, board_path, speed, prob, game_mode):
        """ initializes game's atributes and settings"""
        self.board_path = board_path
        self.speed = speed
        self.prob = prob
        self.game_mode = game_mode
        self.counter = 9
        self.board = Board()
        self.snake = Snake(1, 3, 1, 2, 1, 1)
        self.window = None

    def check_arguments(self):
        """checks game's settings. If something is wrong, it raises error"""
        if match(r"[0-9][.][0-9]+|[1-9]\d*", self.speed) is None:
            raise InvalidArgumentsExpection()
        if match(r"0[.][0-9]+|1", self.prob) is None:
            raise InvalidArgumentsExpection()
        if self.game_mode not in {"special", "normal"}:
            raise InvalidArgumentsExpection()
        self.board.load_from_file(self.board_path)
        self.board.check_board()

    def game_play(self):
        """whole game"""
        # setting the board
        self.board.add_snake(self.snake.coordinates)
        food_place = self.board.generate_food()
        self.board.add_char(food_place, Board.FOOD_CHAR)

        # initializing window
        self.window = Screen(self.board)
        self.window.start_window()
        self.window.show_board()
        self.window.stdscr.refresh()

        # introducing some nessesary variables
        barriers = self.board.barriers()  # pernament list of barriers' coordinates
        special_food_place = None  # first position of special food
        snake_is_invisible = False  # Turns true when snake eats special food
        direction = curses.KEY_RIGHT  # first snake's move direction

        # start the game
        while self.snake.is_alive(barriers) or snake_is_invisible:
            score = self.snake.len() - 3  # game's score

            # generating and adding special food (only when game mode is special)
            if score % 5 == 4 and special_food_place is None and self.game_mode == "special":
                special_food_place = self.board.generate_special_food()
                self.board.add_char(special_food_place, Board.SPECIAL_FOOD_CHAR)

            # generating and adding normal food (if there's no food)
            if food_place is None:
                food_place = self.board.generate_food(self.prob)
                if food_place is not None:
                    self.board.add_char(food_place, Board.FOOD_CHAR)

            # setting snake's move direction
            key = self.window.stdscr.getch()
            direction = self.snake.set_direction(key, direction)

            # snake's move (without deleting a tail)
            self.snake.move(direction)
            self.board.add_char(self.snake.coordinates[0], Board.SNAKE_CHAR)

            # snake eats special food (in this case tail is not deleted)
            if self.snake.coordinates[0] == special_food_place:
                snake_is_invisible = True
                special_food_place = None

            # snake eats normal food (in this case tail is not deleted)
            elif self.snake.coordinates[0] == food_place:
                food_place = None

            # snake doesn't eat anything (in this case tail is deleted)
            else:
                tail = self.snake.coordinates.pop()
                if tail in self.snake.coordinates:
                    self.board.add_char(tail, Board.SNAKE_CHAR)
                elif tail in barriers:
                    self.board.add_char(tail, Board.BARRIER_CHAR)
                else:
                    self.board.add_char(tail, " ")

            # counting the duration of special mode
            if snake_is_invisible:
                self.window.add_char(11, 1, str(self.counter))
                self.counter -= 1

            # ending snake's special mode
            if self.counter == 0:
                self.window.add_char(11, 1, " ")
                snake_is_invisible = False
                self.counter = 9

            # showing board's changes
            self.window.show_board()
            # game's speed
            time.sleep(1 / float(self.speed))

        # Ending the game
        self.window.add_char(5, 8, "Game over!")
        self.window.add_char(6, 8, "Your score = {}".format(score))
        self.window.stdscr.refresh()
        self.window.end_window()
