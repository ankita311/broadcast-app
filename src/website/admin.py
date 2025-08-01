from django.contrib import admin
from .models import Post, Subscription, Notification


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'scheduled_for', 'is_published', 'created_at']
    list_filter = ['is_published', 'scheduled_for', 'created_at']
    search_fields = ['title', 'content', 'author__username']


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ['subscriber', 'author', 'created_at']
    list_filter = ['created_at']
    search_fields = ['subscriber__username', 'author__username']


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ['user', 'post', 'is_read', 'created_at']
    list_filter = ['is_read', 'created_at']
    search_fields = ['user__username', 'message']
