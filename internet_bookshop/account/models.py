from django.db import models
from django.utils import timezone
from django_registration.forms import User


class WebsiteUser(models.Model):
	# USER_TYPE_CHOICES = [
	# 	('a', 'admin'),
	# 	('m', 'manager'),
	# 	('c', 'client'),
	# ]

	user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='username', default='')
	first_name = models.CharField(verbose_name='name', max_length=100)
	last_name = models.CharField(verbose_name='surname', max_length=100)
	patronymic = models.CharField(verbose_name='patronymic', max_length=100, default='', blank=True)
	email = models.EmailField(verbose_name='email')
	phone_number = models.CharField(verbose_name='phone_number', default='', max_length=20, blank=True)
	created_at = models.DateTimeField(default=timezone.now, verbose_name='created_at')
	modified_at = models.DateTimeField(auto_now=True, verbose_name='modified_at')
	avatar = models.FileField(verbose_name='avatar', upload_to='images/', blank=True, null=True)
	# user_role = models.CharField(max_length=1, choices=USER_TYPE_CHOICES, default='c', verbose_name='роль')

	def __str__(self):
		return self.email
