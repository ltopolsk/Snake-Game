from src.game import Game, InvalidArgumentsExpection
from src.board import InvalidBoardException


if __name__ == "__main__":

    all_correct = False
    while not all_correct:
        line = input("Enter path to board, snake's speed, probability of generating food and game mode(normal or special): ")
        arguments = line.split(" ")
        if len(arguments) == 4:
            game1 = Game(*arguments)
            try:
                game1.check_arguments()
                all_correct = True
            except InvalidArgumentsExpection:
                print("Error: one of arguments is wrong")
            except InvalidBoardException:
                print("Error: something is wrong with board")
            except OSError:
                print("Error: something wrong with path to board")
        else:
            print("Error: wrong amout of arguments")
    game1.game_play()
