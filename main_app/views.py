from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Book

class BookCreate(CreateView):
  model = Book
  fields = '__all__'

class BookUpdate(UpdateView):
  model = Book
  fields = '__all__'

class BookDelete(DeleteView):
  model = Book
  success_url = '/books/'

def about(request):
  return render(request, 'about.html')

def books_detail(request, book_id):
  print(book_id)
  book = Book.objects.get(id=book_id)
  return render(request, 'books/detail.html', { 'book': book })

def books_index(request):
  books = Book.objects.all()
  return render(request, 'books/index.html', { 'books': books })

def home(request):
  return render(request, 'home.html')