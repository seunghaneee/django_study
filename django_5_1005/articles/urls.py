from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    # create
    # path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    # read
    path('<int:article_pk>/', views.detail, name='detail'),
    # delete
    path('<int:article_pk>/delete/', views.delete, name='delete'),
    # update
    # path('<int:article_pk>/edit/', views.edit, name='edit'),
    path('<int:article_pk>/update/', views.update, name='update'),

    path('<int:article_pk>/comments/', views.comments_create, name='comments_create'),
    path('<int:article_pk>/comments/<int:comment_pk>/delete/', views.comments_delete, name='comments_delete'),

]
