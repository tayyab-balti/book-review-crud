from django.urls import path
from . import views

urlpatterns = [
    path('', views.books_list, name='books-list'),
    path('book-detail/<int:pk>/', views.book_detail, name='book-detail'),
    path('book/new/', views.book_create, name='book-create'),
    path('book/<int:pk>/edit/', views.book_update, name='book-update'),
    path('book/<int:pk>/delete/', views.book_delete, name='book-delete'),
]