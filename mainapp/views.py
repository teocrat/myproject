import logging
from django.shortcuts import render
from django.http import HttpResponse
from random import choice
from mainapp.models import GameModel, Author, Post


logger = logging.getLogger(__name__)


def index(request):
    logger.info("Index page accessed")
    return HttpResponse("Hello, world.")


def main(request):
    logger.info("Main page accessed")
    return render(request, 'main.html')


def about(request):
    logger.info("About page accessed")
    return render(request, 'about_me.html')


def play(request):
    result = choice(['орел', 'решка'])

    game = GameModel(result=result)
    game.save()

    return HttpResponse(f'{result}')


def last_game(request):
    last = GameModel().return_last(7)
    res = ['<br>' + str(i) for i in last]
    return HttpResponse(res)


def author(request):
    auth = Author.objects.all()
    res = [str(i) + '<br>' for i in auth]
    return HttpResponse(res)


def post(request):
    post = Post.objects.all()[:10]
    res = [str(i) + '<br>' for i in post]
    return HttpResponse(res)
