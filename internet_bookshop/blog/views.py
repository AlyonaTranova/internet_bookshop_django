from django.shortcuts import render
from django.views.generic import View, DetailView, ListView
from django.views.generic.edit import FormMixin
from .models import Post, Comment, Tag


class PostListView(ListView):
	model = Post
	template_name = 'blog.html'
	# paginate_by = 3
	context_object_name = 'posts'

	def get_queryset(self, *args, **kwargs):
		queryset = super(PostListView, self).get_queryset().order_by('id')
		sort = self.request.GET.get('sort')
		tags = self.request.GET.get('tag')

		if sort == 'date':
			return queryset.order_by('created_at')
		elif sort == '-date':
			return queryset.order_by('-created_at')
		elif sort == 'tag_filter':
			print(tags)
			return queryset.filter(tag__tag=tags)
		else:
			return queryset

	def get_context_data(self, **kwargs):
		context = super(PostListView, self).get_context_data(**kwargs)
		context.update({
			'tags': Tag.objects.all()
		})
		return context


class PostDetailView(DetailView):
	model = Post
	template_name = 'blog-detail.html'
	slug_url_kwarg = 'slug'
	context_object_name = 'post'
