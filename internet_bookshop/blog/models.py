from django.utils import timezone
from django.db import models
from django.urls import reverse


class Tag(models.Model):
	tag = models.CharField(max_length=100, verbose_name='tag', default='')

	def __str__(self):
		return self.tag


class Post(models.Model):
	title = models.CharField(max_length=200, verbose_name='title')
	text = models.TextField(verbose_name='text')
	created_at = models.DateTimeField(default=timezone.now, verbose_name='created at')
	modified_at = models.DateTimeField(auto_now=True, verbose_name='modified at')
	tag = models.ManyToManyField(Tag, related_name='tags')
	slug = models.SlugField(max_length=100, unique=True, null=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('post', args=[self.slug])


class Comment(models.Model):
	pass
