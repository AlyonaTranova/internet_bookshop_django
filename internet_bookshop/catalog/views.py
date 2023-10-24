from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import View, DetailView, ListView
from .models import Book, Genre
from django.apps import apps


class BaseView(View):
	def get(self, request):
		post = apps.get_model('blog', 'Post')
		print(post)
		new_books = Book.objects.all().order_by('created_at')[:3]
		posts = post.objects.all().order_by('created_at')[:3]
		return render(request, 'mainpage.html', context={'books': new_books, 'posts': posts})


def book_list(request):
	books = Book.objects.all()
	return render(request, 'catalog.html', {'books': books})


class CatalogListView(ListView):
	model = Book
	template_name = 'catalog.html'
	context_object_name = 'books'
	paginate_by = 4

	def get_queryset(self, *args, **kwargs):
		queryset = super(CatalogListView, self).get_queryset().order_by('id')
		sort = self.request.GET.get('sort')
		start_price = self.request.GET.get('start')
		end_price = self.request.GET.get('end')
		genre_name = self.request.GET.get('genre')

		# print(f'sort: {sort}, queryset: {queryset}')

		if sort == 'price':
			return queryset.order_by('price')
		elif sort == '-price':
			return queryset.order_by('-price')
		elif sort == 'name':
			return queryset.order_by('title')

		elif sort == 'price_filter':
			if not start_price and not end_price:
				return queryset.filter(price__gte=0)
			elif not start_price:
				return queryset.filter(price__lte=end_price)
			elif not end_price:
				return queryset.filter(price__gte=start_price)
			else:
				return queryset.filter(price__gte=start_price, price__lte=end_price)

		elif sort == 'genre_filter':
			return queryset.filter(genre__genre_name=genre_name)

		else:
			return queryset

	def get_context_data(self, **kwargs):
		context = super(CatalogListView, self).get_context_data(**kwargs)
		context.update({
			'genres': Genre.objects.all(),
		})
		return context


class CatalogDetailView(DetailView):
	model = Book
	template_name = 'catalog_detail.html'
	slug_url_kwarg = 'slug'
	context_object_name = 'book'
