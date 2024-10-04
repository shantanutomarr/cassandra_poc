from django.urls import path
from sample_app.views import list_books, create_book, update_book, BookDeleteView


app_name = "books"

urlpatterns = [
    path('', list_books, name='list'),
    path('create/', create_book, name='create'),
    path('<uuid:book_id>/', update_book, name='update'),
    path('delete/<uuid:book_id>/', BookDeleteView.as_view(), name='delete'),
]
