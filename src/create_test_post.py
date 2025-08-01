#!/usr/bin/env python
import os
import django
from datetime import timedelta

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'broadcast.settings')
django.setup()

from django.contrib.auth.models import User
from django.utils import timezone
from website.models import Post

def create_test_post():
    print("Creating test post...")
    
    # Get or create a test user
    user, created = User.objects.get_or_create(
        username='testuser',
        defaults={'email': 'test@example.com'}
    )
    if created:
        user.set_password('testpass123')
        user.save()
        print(f"Created user: {user.username}")
    else:
        print(f"Using existing user: {user.username}")
    
    # Create a post scheduled for 1 minute from now
    scheduled_time = timezone.now() + timedelta(minutes=1)
    
    post = Post.objects.create(
        author=user,
        title='Test Post - Auto Publishing',
        content='This is a test post to verify automatic publishing works!',
        scheduled_for=scheduled_time,
        is_published=False
    )
    
    print(f"Created post: {post.title}")
    print(f"Scheduled for: {post.scheduled_for}")
    print(f"Current time: {timezone.now()}")
    print(f"Will be published in: {scheduled_time - timezone.now()}")
    
    return post

if __name__ == "__main__":
    create_test_post() 