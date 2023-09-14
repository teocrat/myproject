from django.urls import path

from mainapp import views
import playapp.views

urlpatterns = [
    path('', views.MainView.as_view(), name='index'),
    path('play/', views.PlayView.as_view(), name='play'),
    path('last/', playapp.views.last_game, name='last'),
    path('author/', views.author, name='author'),
    path('post/', views.post, name='post'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('heads/', views.HeadsView.as_view(), name='heads'),
    path('cube/', views.CubeView.as_view(), name='cube'),
    path('ran_num/', views.RanNum.as_view(), name='ran_num'),
    path('heads_game/<int:count>', views.HeadsGame.as_view(), name='heads_game'),
    path('cube_game/<int:count>', views.CubeGame.as_view(), name='cube_game'),
    path('ran_num_game/<int:count>',
         views.RanNumGame.as_view(), name='ran_num_game'),
    path('posts/<int:id>', views.AllPosts.as_view(), name='posts'),
    path('detail_post/<int:pk>', views.DetailPost.as_view(), name='detail_post'),
    path('orders/<int:id>', views.AllOrders.as_view(), name='orders'),
    path('products/<int:id>/<int:count>', views.AllProducts.as_view(), name='products'),
    path('add_author/', views.AddAuthor.as_view(), name='add_author'),
    path('author_page/<int:pk>', views.AuthorPage.as_view(), name='author_page'),
    path('add_post/', views.AddPost.as_view(), name='add_post'),
    path('prod_detail/', views.ProductDetailView.as_view(), name='prod_detail'),
    path('prod_edit/<int:pk>/',views.ProductUpdateView.as_view(), name='prod_edit'),
    
    
]

