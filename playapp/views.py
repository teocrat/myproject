import logging
from django.http import HttpResponse
from random import choice, randint


logger = logging.getLogger(__name__)


def heads_tails(request):
    res = choice(['орел', 'решка'])
    logger.info(f'Результат: {res}')
    return HttpResponse(res)

def cube(request):
    res = randint(1, 6)
    logger.info(f'Результат: {res}')
    return HttpResponse(res)


def ran_num(request):
    res = randint(1, 100)
    logger.info(f'Результат: {res}')
    return HttpResponse(res)
