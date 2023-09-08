from django.urls import path
from playapp import views

urlpatterns = [
    path('heads_tails/', views.heads_tails, name='heads_tails'),
    path('cube/', views.cube, name='cube'),
    path('ran_num', views.ran_num, name='ran_num'),

    ]