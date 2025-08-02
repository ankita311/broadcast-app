from django.contrib import admin
from .models import Post, Subscription, Notification

admin.site.register(Post)
admin.site.register(Subscription)
admin.site.register(Notification)
