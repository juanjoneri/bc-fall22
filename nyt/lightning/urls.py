from django.urls import path
from . import views

urlpatterns = [
    path('articles/', views.index, name='index'),
    path('articles/<int:article_id>', views.article, name='article'),
    path('signup/', views.signup, name='signup'),
    path('publish/', views.article_form, name='publish'),
    path('home/', views.home, name='index'),
]