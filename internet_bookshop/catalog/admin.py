from django.contrib import admin

from .models import Book, BookImage, Author, Genre, Publisher


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
	list_display = ['id', 'title', 'author', 'description', 'publisher', 'quantity_available', 'price']
	list_filter = ['title']
	search_fields = ['title', 'author', 'publisher']
	prepopulated_fields = {'slug': ('title',)}


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
	list_display = ['id', 'name']
	search_fields = ['name']


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
	list_display = ['id', 'genre_name']
	search_fields = ['genre_name']


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
	list_display = ['id', 'publisher_name']
	search_fields = ['publisher_name']
