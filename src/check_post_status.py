#!/usr/bin/env python
import os
import django

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'broadcast.settings')
django.setup()

from django.utils import timezone
from website.models import Post

def check_post_status():
    print("Checking post status...")
    print(f"Current time: {timezone.now()}")
    
    # Get all posts
    posts = Post.objects.all().order_by('-created_at')
    
    for post in posts:
        print(f"\nPost: {post.title}")
        print(f"Author: {post.author.username}")
        print(f"Created: {post.created_at}")
        print(f"Scheduled for: {post.scheduled_for}")
        print(f"Is published: {post.is_published}")
        print(f"Content: {post.content[:50]}...")
    
    # Check for posts that should be published
    now = timezone.now()
    posts_to_publish = Post.objects.filter(
        scheduled_for__lte=now,
        is_published=False
    )
    
    print(f"\nPosts that should be published: {posts_to_publish.count()}")
    for post in posts_to_publish:
        print(f"- {post.title} (scheduled for {post.scheduled_for})")

if __name__ == "__main__":
    check_post_status() 