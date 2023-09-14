from django.urls import path
from gameapp import views

urlpatterns = [
    path('games/', views.game_view, name='game_view'),
]