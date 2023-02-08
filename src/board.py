from random import choice
from random import randint


class InvalidBoardException(Exception):
    pass


class Board():
    """
    Board class. Has atributes:
    :table: list

    table contains game board in two dimensional list (10 rows and 25 collumns)
    Food char is sign used to mark the food
    Special food char is sign used to mark special food (special food allows player to go through snake's body and barriers)
    Barrier char is sign used to mark barriers
    Snake char is sign used to mark snake
    """
    HEIGHT = 10
    WIDTH = 25
    FOOD_CHAR = "A"
    SPECIAL_FOOD_CHAR = "E"
    BARRIER_CHAR = "#"
    SNAKE_CHAR = "S"

    def __init__(self):
        """ initializes board"""
        self.table = []

    def load_from_file(self, path_to_file):
        """ 
        loads board from text file.
        If path to file is wrong, raises OS error
        """
        try:
            with open(path_to_file) as file:
                self.table = [list(line.rstrip("\n")) for line in file]
        except OSError as e:
            raise e

    def check_board(self):
        """
        checks board width, height and every sign. Allowed signs: " ", Board.BARRIER_CHAR.
        Raises error if something is incorrect
        """
        if len(self.table) != Board.HEIGHT:
            raise InvalidBoardException("Error: Wrong height of board")
        for line in self.table:
            if len(line) != Board.WIDTH:
                raise InvalidBoardException("Error: Wrong width of board")
            for char in line:
                if char not in {" ", Board.BARRIER_CHAR}:
                    raise InvalidBoardException("Error: Wrong signs in board")

    def empty_places(self):
        """
        Returns list of coordinates, in which are empty places.
        Used in generating food
        """
        empty_places = []
        for row in range(Board.HEIGHT):
            for column in range(Board.WIDTH):
                if self.table[row][column] == " ":
                    empty_places.append(tuple((row, column)))
        return empty_places

    def barriers(self):
        """
        Returns list of coordinates, in which are barriers.
        Used in checking if snake is alive
        """
        barriers = []
        for row in range(Board.HEIGHT):
            for column in range(Board.WIDTH):
                if self.table[row][column] == Board.BARRIER_CHAR:
                    barriers.append(tuple((row, column)))
        return barriers

    def generate_food(self, prob="1"):
        """
        Returns coordiantes of randomly generated food.
        Prob is chance to generate food every snake's step.
        """
        if prob == "1":
            new_prob = prob
        else:
            new_prob = prob.split(".")[1]
        number = randint(1, 10**len(new_prob))
        if number in range(1, int(new_prob)+1) or int(new_prob) == 1:
            food_place = choice(self.empty_places())
        else:
            food_place = None
        return food_place

    def generate_special_food(self):
        """
        Returns coordinates of randomly generated special food
        """
        return self.generate_food()

    def add_snake(self, snake_cordinates):
        """
        Adds snake to board.
        """
        for coordinates in snake_cordinates:
            self.add_char(coordinates, Board.SNAKE_CHAR)

    def add_char(self, coordinates, char):
        """
        puts char in place (defined by coordinates) on board
        """
        self.table[coordinates[0]][coordinates[1]] = char
