from django.urls import path
from django.conf.urls import url
from .views import PostListView, PostDetailView

urlpatterns = [
	path('blog', PostListView.as_view(), name='posts'),
	path('blog/<slug:slug>/', PostDetailView.as_view(), name='post'),
]
