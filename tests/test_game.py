from src.game import Game, InvalidArgumentsExpection
import pytest

game1 = Game("Example.txt", "-5", "0.5", "special")
game2 = Game("Example.txt", "5", "p", "normal")
game3 = Game("Example.txt", "1.5", "0.5", "snake1")


def test_invalid_arguments():
    with pytest.raises(InvalidArgumentsExpection):
        game1.check_arguments()
        game2.check_arguments()
        game3.check_arguments()
