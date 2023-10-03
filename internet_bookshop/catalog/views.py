from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import View, generic
from .models import Book


class BaseView(View):
	def get(self, request):
		new_books = Book.objects.all().order_by('created_at')[:3]
		return render(request, 'mainpage.html', context={'books': new_books})


def book_list(request):
	books = Book.objects.all()
	return render(request, 'catalog.html', {'books': books})


def book_detail(request, book_slug):
	book = get_object_or_404(Book, slug=book_slug)
	return render(request, 'catalog_detail.html', {'book': book})
