from django.urls import path,include
from .views import home
from .views import create
from .views import search
from .views import getbooks
from .views import get_books_by_language
from .views import get_books_by_genre
from .views import get_books_by_genandlang
from .views import add_book

urlpatterns = [
    path('', home, name='home'),
    path('create/', create, name='create'),
    path('search/', search, name='search'),
    path("getbooks/", getbooks, name="getbooks"),
    path('getbooks/lang/', get_books_by_language, name='get_books_by_language'),
    path('getbooks/genr/', get_books_by_genre, name='get_books_by_genre'),
    path("getbooks/filter/", get_books_by_genandlang, name="get_books_by_genandlang"),
    path("api/add_book/", add_book, name="add_book")
]
