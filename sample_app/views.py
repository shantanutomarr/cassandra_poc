from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, CreateView, UpdateView

from .models import Book
from .forms import BookForm


class BooksListView(ListView):
    model = Book
    template_name = 'book_list.html'
    context_object_name = "books"


class CreateBookView(CreateView):
    model = Book
    template_name = 'book_form.html'
    form_class = BookForm
    success_url = reverse_lazy('books:list')


class UpdateBookView(UpdateView):
    model = Book
    template_name = 'book_form.html'
    form_class = BookForm
    success_url = reverse_lazy('books:list')
    pk_url_kwarg = "book_id"
  
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["book"] = self.object
        return context


class BookDeleteView(DeleteView):
    model = Book
    pk_url_kwarg = "book_id"
    template_name = 'book_confirm_delete.html'
    success_url = reverse_lazy('books:list')
