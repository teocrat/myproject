import logging
from typing import Any
from django.db import models
from django.shortcuts import render
from django.http import HttpResponse
from mainapp.models import GameModel, Author, Post, Buyer, Orders
from django.views.generic import TemplateView, DetailView
from random import choice, randint


logger = logging.getLogger(__name__)


def author(request):
    auth = Author.objects.all()
    res = [str(i) + '<br>' for i in auth]
    return HttpResponse(res)


def post(request):
    post = Post.objects.all()[:10]
    res = [str(i) + '<br>' for i in post]
    return HttpResponse(res)


def last_game(request, count):
    last = GameModel().return_last(count)
    result = ['<br>' + str(i) for i in last]
    return HttpResponse(result)


class MainView(TemplateView):
    template_name = 'mainapp/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Main page'
        return context


class AboutView(TemplateView):
    template_name = 'mainapp/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'About me'
        return context


class PlayView(TemplateView):
    template_name = 'mainapp/play.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Play'
        return context


class HeadsView(TemplateView):
    template_name = 'mainapp/heads.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        result = choice(['орел', 'решка'])
        logger.info(f'Результат: {result}')

        game = GameModel(result=result)
        game.save()

        context['title'] = 'Heads or tails'
        context['result'] = result
        return context


class CubeView(TemplateView):
    template_name = 'mainapp/cube.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        result = randint(1, 6)
        logger.info(f'Результат: {result}')

        game = GameModel(result=result)
        game.save()

        context['title'] = 'Cube'
        context['result'] = result
        return context


class RanNum(TemplateView):
    template_name = 'mainapp/ran_num.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        result = randint(1, 100)
        logger.info(f'Результат: {result}')

        game = GameModel(result=result)
        game.save()

        context['title'] = 'Random number'
        context['result'] = result
        return context


class GameView(TemplateView):
    template_name = 'mainapp/game.html'


class HeadsGame(GameView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        results = [choice(['орел', 'решка'])
                   for _ in range(self.kwargs['count'])]
        context['results'] = results
        context['title'] = 'Heads or tails'
        return context


class CubeGame(GameView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        results = [randint(1, 6) for _ in range(int(self.kwargs['count']))]
        context['results'] = results
        context['title'] = 'Cube'
        return context


class RanNumGame(GameView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        results = [randint(1, 100) for _ in range(int(self.kwargs['count']))]
        context['results'] = results
        context['title'] = 'Random number'
        return context


class AllPosts(TemplateView):
    template_name = 'mainapp/posts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        author = Author.objects.get(pk=self.kwargs['id'])
        posts = Post.objects.filter(author=author.id).all()
        context['posts'] = posts
        context['title'] = f'Author{author.id} posts'
        return context
    
class DetailPost(DetailView):
    model = Post
    template_name = 'mainapp/detail_post.html'
    context_object_name = 'post'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        obj.viewed +=1
        obj.save()
        return obj
    


class AllOrders(TemplateView):
    template_name = 'mainapp/orders.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        client = Buyer.objects.get(pk=self.kwargs['id'])
        orders = Orders.objects.filter(client=client.id).all()
        context['orders'] = orders
        context['title'] = f'Buyer{client.id} orders'
        return context
    

class AllProducts(TemplateView):
    template_name = 'mainapp/products.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        client = Buyer.objects.get(pk=self.kwargs['id'])
        count = self.kwargs['count']
        orders = Orders().return_last(count)
        context['orders'] = orders
        context['title'] = f'Buyer{client.id} products'
        return context
    

