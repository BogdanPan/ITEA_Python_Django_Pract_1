from .views import index, article, articles
from django.urls import path, include


urlpatterns = [
    path('', index, name='index', ),
    path('posts/<slug:article_slug>', article, name='articles-article'),
    path('posts/', articles, name='articles'),
]
