from django.urls import path

from . import views

urlpatterns = [
    path('articles/', views.index, name='index'),
    path('articles/<int:article_id>', views.article, name='article'),
]