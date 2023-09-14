from random import choice, randint


class Game:
    def __init__(self):
        self.result = None

    def play(self):
        pass

    def __str__(self):
        return str(self.result)


class HeadsOrTails(Game):
    def play(self):
        self.result = choice(['Heads', 'Tails'])


class Cube(Game):
    def play(self):
        self.result = randint(1, 6)


class RanNum(Game):
    def play(self):
        self.result = randint(1, 100)
