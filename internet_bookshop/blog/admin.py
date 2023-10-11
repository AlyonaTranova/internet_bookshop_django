from django.contrib import admin
from .models import Tag, Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	list_display = ['id', 'title', 'text', 'slug', 'created_at']
	list_filter = ['title']
	prepopulated_fields = {'slug': ('title',)}


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
	list_display = ['id', 'tag']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
	list_display = ['id', 'rating', 'text', 'active', 'user_id', 'post_id']