from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('news/', views.news, name='news'),
    path('my-game/', views.my_game, name='my-game'),
    path('about-us/', views.about_us, name='about-us'),
]