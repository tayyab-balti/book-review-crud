from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm
from django.contrib import messages
from django.urls import reverse

def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Book created successfully!!")
            return redirect('book-create')
    else:
        form = BookForm()
    return render(request, 'book/book_form.html', {'form':form})

def books_list(request):
    genre = request.GET.get('genre')
    if genre:
        books = Book.objects.filter(genre=genre).order_by('-created_at')
    else:
        books = Book.objects.all().order_by('-created_at')
    return render(request, 'book/books_list.html', {'books':books})

def book_detail(request, pk):
    book = Book.objects.get(pk=pk)
    return render(request, 'book/book_detail.html', {'book':book})

def book_update(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)   # gets the id of the book
        if form.is_valid():
            form.save()
            messages.success(request, 'Book updated successfully!!')
            return redirect('book-update', pk=book.pk)
    else:
        form = BookForm(instance=book)
    context = {
        'form':form, 
        'back_url': reverse('book-detail', kwargs={'pk':book.pk}),
        'is_editing':True    # <- flag to indicate we're editing
        }
    return render(request, 'book/book_form.html', context)

def book_delete(request, pk):
    book = Book.objects.get(pk=pk)
    # if request.method == "POST":
        # if form.is_valid():
    book.delete()
    messages.success(request, "Book deleted successfully!!")
    return redirect('books-list')