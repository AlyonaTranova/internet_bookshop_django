from django.db import models
from django.urls import reverse
from django.utils import timezone


# TODO добавить related names and check connection between models
# TODO check how it works with media and images of books

class Author(models.Model):
	name = models.CharField(max_length=100, verbose_name='author')

	def __str__(self):
		return self.name


class Genre(models.Model):
	genre_name = models.CharField(max_length=100, verbose_name='genre')

	def __str__(self):
		return self.genre_name


class Publisher(models.Model):
	publisher_name = models.CharField(max_length=100, verbose_name='publisher')

	def __str__(self):
		return self.publisher_name


class Book(models.Model):
	title = models.CharField(max_length=100, verbose_name='book title', default='')
	author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='author')
	description = models.TextField(verbose_name='description', default='')
	genre = models.ForeignKey(Genre, on_delete=models.CASCADE, verbose_name='genre')
	publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, verbose_name='publisher')
	quantity_available = models.IntegerField(verbose_name='quantity', default=0)
	price = models.DecimalField(verbose_name='price', default=0.00, max_digits=10, decimal_places=2)
	created_at = models.DateTimeField(default=timezone.now, verbose_name='created at')
	modified_at = models.DateTimeField(auto_now=True, verbose_name='modified at')
	slug = models.SlugField(max_length=100, unique=True, null=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('book', args=[self.slug])


def product_images_directory_path(instance: "BookImage", filename: str) -> str:
	return "books/book_{pk}/images/{filename}".format(pk=instance.book.pk, filename=filename)


class BookImage(models.Model):
	book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name='book', related_name='images')
	img = models.FileField(verbose_name='image', upload_to=product_images_directory_path, null=True, blank=True)
