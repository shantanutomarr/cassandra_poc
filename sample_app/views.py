from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.views.generic import DeleteView

from .models import Book
from .forms import BookForm


def list_books(request):
    return render(request, 'book_list.html', {'books': Book.objects.all()})


def create_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Book created successfully.")
            return redirect('books:list')
    else:
        form = BookForm()

    return render(request, 'book_form.html', {'form': form})


def update_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save() 
            messages.success(request, "Book updated successfully.")
            return redirect('books:list')
    else:
        form = BookForm(instance=book)

    return render(request, 'book_form.html', {'form': form, 'book': book})


class BookDeleteView(DeleteView):
    model = Book
    pk_url_kwarg = "book_id"
    template_name = 'book_confirm_delete.html'
    success_url = reverse_lazy('books:list')
