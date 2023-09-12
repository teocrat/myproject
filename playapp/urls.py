from django.urls import path
from playapp import views

urlpatterns = [
    # path('heads/', views.heads_tails, name='heads'),
    path('cube/', views.cube, name='cube'),
    path('ran_num/', views.ran_num, name='ran_num'),

    ]