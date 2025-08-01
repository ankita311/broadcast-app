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

def create_immediate_post():
    print("Creating immediate post...")
    
    # Get or create a test user
    user, created = User.objects.get_or_create(
        username='testuser',
        defaults={'email': 'test@example.com'}
    )
    
    # Create a post scheduled for 1 minute ago (should be published immediately)
    scheduled_time = timezone.now() - timedelta(minutes=1)
    
    post = Post.objects.create(
        author=user,
        title='Immediate Test Post',
        content='This post should be published immediately!',
        scheduled_for=scheduled_time,
        is_published=False
    )
    
    print(f"Created post: {post.title}")
    print(f"Scheduled for: {post.scheduled_for}")
    print(f"Current time: {timezone.now()}")
    print(f"Should be published immediately!")
    
    return post

if __name__ == "__main__":
    create_immediate_post() 