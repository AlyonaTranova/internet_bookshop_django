from django.contrib import admin
from .models import WebsiteUser


@admin.register(WebsiteUser)
class ClientAdmin(admin.ModelAdmin):
	list_display = [
		'id', 'user', 'first_name', 'last_name', 'email', 'phone_number', 'created_at', 'modified_at', 'avatar'
	]
	search_fields = [
		'last_name', 'email'
	]
	fieldsets = (
		('Имя клиента', {
			'fields': ('user', 'first_name', 'last_name', 'patronymic', 'avatar')
		}),
		('Контактные данные', {
			'fields': ('email', 'phone_number')
		})
	)


