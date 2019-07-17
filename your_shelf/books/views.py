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
# BookDetail
from django.views.generic import DetailView

def index(request):
    book_list = Book.objects.order_by('-publish_date')[:5]
    return render(request, 'books/book_list.html', {'book_list':book_list})

# def book_detail(request, book_title):
#     book = Book.objects.get(title=book_title)
#     return render(request, 'books/book_detail.html', {'book':book})
class BookDetail(DetailView):
    model = Book
    template_name = 'books/book_detail.html'

class BookCreate(CreateView):
    model = Book
    template_name = 'books/book_create.html'
    success_url = reverse_lazy('books:index')
    # success_url = reverse_lazy('books:detail', kwargs={'book_title': Book.objects.get(title=book_title)})

    fields = ['attrs', 'owner', 'borrower', 'title', 'isbn', 'image',\
     'author', 'price', 'publisher', 'publish_date', 'description']

    def form_valid(self, form):
        result = super().form_valid(form)
        messages.success(
            self.request, '「{}」Created!'.format(form.instance))
        return result

class BookUpdate(UpdateView):
    model = Book
    template_name = 'books/book_update.html'
    # success_url = reverse_lazy('books:detail', kwargs={'book_title': Book.objects.get(title=book_title)})
    success_url = reverse_lazy('books:index')
    fields = ['attrs', 'owner', 'borrower', 'title', 'isbn', 'image',\
     'author', 'price', 'publisher', 'publish_date', 'description']
    tempalte_name_suffix = '_update_form'

    # def get(self, request, book_title):

class BookDelete(DeleteView):
    model = Book
    template_name = 'books/book_delete.html'
    success_url = reverse_lazy('books:index')
