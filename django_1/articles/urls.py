from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    # path('articles/', views.index),
    path('index/', views.index, name='index'),
    path('greeting/', views.greeting, name='greeting'),
    path('dinner/', views.dinner, name='dinner'),
    path('throw/', views.throw, name='throw'),
    path('catch/', views.catch, name='catch'),
    # path('hello/<str:name>/', views.hello),
    path('hello/<name>/', views.hello, name='hello'),
]
