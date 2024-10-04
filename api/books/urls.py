from django.urls import path
from api.books.views import BooksListCreateAPIView


app_name = "api_books"

urlpatterns = [
    path('', BooksListCreateAPIView.as_view(), name='list_create'),
]
