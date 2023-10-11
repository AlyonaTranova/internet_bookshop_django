from django.utils import timezone
from django.db import models
from django.urls import reverse
from django_registration.forms import User


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
	post_rating = [
		(1, '1'),
		(2, '2'),
		(3, '3'),
		(4, '4'),
		(5, '5'),
	]
	user_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='user', default='')
	post_id = models.ForeignKey(
		Post, on_delete=models.CASCADE, verbose_name='post', default='', related_name='comments'
	)
	text = models.TextField(verbose_name='text', default='')
	rating = models.IntegerField(choices=post_rating, default=1, verbose_name='rating')
	created_at = models.DateTimeField(default=timezone.now, verbose_name='created_at')
	modified_at = models.DateTimeField(auto_now=True, verbose_name='modified_at')
	active = models.BooleanField(default=True)

	def __str__(self):
		return 'Comment by {} on {}'.format(self.user_id, self.post_id)
