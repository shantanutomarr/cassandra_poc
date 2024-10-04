from django.urls import path
from sample_app.views import BooksListView, CreateBookView, UpdateBookView, BookDeleteView


app_name = "books"

urlpatterns = [
    path('', BooksListView.as_view(), name='list'),
    path('create/', CreateBookView.as_view(), name='create'),
    path('<uuid:book_id>/', UpdateBookView.as_view(), name='update'),
    path('<uuid:book_id>/delete/', BookDeleteView.as_view(), name='delete'),
]
