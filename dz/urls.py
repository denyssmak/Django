from django.urls import include, path
from .views import index, articles, articles_arhive, users, article, article_num, article_num_arhive, article_num_slug, users_num

urlpatterns = [
    path('', index, name='index'),
    path('articles/', articles, name='articles'),
    path('articles/arhive/', articles_arhive, name='articles_arhive'),\
    path('users/', users, name='users'),
    path('article/', article, name='article'),
    path('article/<int:article_number>/', article_num, name='article_num'),
    path('article/<int:article_number>/arhive/', article_num_arhive, name='article_num_arhive'),
    path('article/<int:article_number>/<slug:slug_text>/', article_num_slug, name='article_num'),
    path('users/<int:user_number>', users_num, name='users_num')
]