from rest_framework.generics import ListCreateAPIView

from sample_app.models import Book
from api.books.serializers import BookSerializer


class BooksListCreateAPIView(ListCreateAPIView):
    model = Book
    serializer_class = BookSerializer
    queryset = Book.objects.all()