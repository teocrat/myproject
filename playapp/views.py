import logging
from django.http import HttpResponse
from random import choice, randint
from mainapp.models import GameModel


logger = logging.getLogger(__name__)


def heads_tails(request):
    result = choice(['орел', 'решка'])
    logger.info(f'Результат: {result}')

    game = GameModel(result=result)
    game.save()

    return HttpResponse(f'{result}')


def last_game(request):
    last = GameModel().return_last(7)
    res = ['<br>' + str(i) for i in last]
    return HttpResponse(res)


def cube(request):
    res = randint(1, 6)
    logger.info(f'Результат: {res}')
    return HttpResponse(res)


def ran_num(request):
    res = randint(1, 100)
    logger.info(f'Результат: {res}')
    return HttpResponse(res)
