from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


def post_upload_path(instance, filename):
    """Simple file upload path for posts"""
    return f'posts/{instance.author.username}/{filename}'


class Post(models.Model):
    """Simple post model with scheduled publishing"""
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to=post_upload_path, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    scheduled_for = models.DateTimeField()
    is_published = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.title} by {self.author.username}"


class Subscription(models.Model):
    """Simple subscription model"""
    subscriber = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscriptions')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscribers')
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ['subscriber', 'author']
    
    def __str__(self):
        return f"{self.subscriber.username} follows {self.author.username}"


class Notification(models.Model):
    """Simple notification model"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    message = models.CharField(max_length=500)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Notification for {self.user.username}: {self.message[:50]}"
