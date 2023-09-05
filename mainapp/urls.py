from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('main/', views.main, name='main'),
    path('play/', views.play, name='play'),
    path('last/', views.last_game, name='last'),
    path('author/', views.author, name='author'),
    path('post/', views.post, name='post'),
]
