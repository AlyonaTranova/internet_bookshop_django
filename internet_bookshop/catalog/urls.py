from django.urls import path
from django.conf.urls import url
from .views import BaseView, book_list, book_detail

urlpatterns = [
	path('', BaseView.as_view(), name='main'),
	path('catalog', book_list, name='books'),
	path('catalog/<slug:book_slug>/', book_detail, name='book'),
]
