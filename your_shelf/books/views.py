from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
# + book_admin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import BookForm
from django.http import HttpResponse
from django.urls import reverse_lazy
from .models import Book
from django.contrib import messages

def index(request):
    book_list = Book.objects.order_by('-publish_date')[:5]
    return render(request, 'books/book_list.html', {'book_list':book_list})

def book_detail(request, book_title):
    book = Book.objects.get(title=book_title)
    return render(request, 'books/book_detail.html', {'book':book})

class BookCreate(CreateView):
    template_name = 'books/book_create.html'
    model = Book
    success_url = reverse_lazy('books:index')
    # success_url = reverse_lazy('books:detail', kwargs={'book_title': Book.objects.get(title=book_title)})

    fields = ['owner', 'borrower', 'title', 'isbn', 'image',\
     'author', 'price', 'publisher', 'publish_date', 'description']

    def form_valid(self, form):
        result = super().form_valid(form)
        messages.success(
            self.request, '「{}」Created!'.format(form.instance))
        return result

class BookUpdate(UpdateView):
    template_name = 'books/book_update.html'
    model = Book
    # success_url = reverse_lazy('books:detail', kwargs={'book_title': Book.objects.get(title=book_title)})
    success_url = reverse_lazy('books:index')
    fields = ['owner', 'borrower', 'title', 'isbn', 'image',\
     'author', 'price', 'publisher', 'publish_date', 'description']
    tempalte_name_suffix = '_update_form'

    # def get(self, request, book_title):

class BookDelete(DeleteView):
    template_name = 'books/book_delete.html'
    model = Book
    success_url = reverse_lazy('books:index')
