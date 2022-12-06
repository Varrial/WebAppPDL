from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('news/', views.news, name='news'),
    path('my-game/', views.my_game, name='my-game'),
    path('about-us/', views.about_us, name='about-us'),
    path('search/', views.search, name='search'),
    path('contact/', views.contact, name='contact'),
    path('faq/', views.faq, name='faq'),
    path('support/', views.support, name='support'),
]