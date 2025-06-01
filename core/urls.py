from django.urls import path
from .views import create_book

urlpatterns = [
    path('create-book/', create_book),
]
