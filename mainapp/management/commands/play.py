from django.core.management import BaseCommand
from random import choice
from mainapp.models import GameModel


class Command(BaseCommand):
    help = "Play game Heads and Tails"

    def handle(self, *args, **kwargs):
        result = choice(['орел', 'решка'])
        game = GameModel(result=result)
        game.save()

        self.stdout.write(f'{result}')


        