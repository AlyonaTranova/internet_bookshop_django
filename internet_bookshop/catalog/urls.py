from django.urls import path
from django.conf.urls import url
from .views import BaseView, CatalogListView, CatalogDetailView

urlpatterns = [
	path('', BaseView.as_view(), name='main'),
	path('catalog', CatalogListView.as_view(), name='books'),
	path('catalog/<slug:slug>/', CatalogDetailView.as_view(), name='book'),
]
