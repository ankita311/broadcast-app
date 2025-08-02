from celery import shared_task
from django.utils import timezone
from .models import Post, Subscription, Notification


@shared_task
def publish_scheduled_posts_task():
    """Celery task to publish scheduled posts"""
    now = timezone.now()
    posts_to_publish = Post.objects.filter(
        scheduled_for__lte=now,
        is_published=False
    )
    
    published_count = 0
    for post in posts_to_publish:
        post.is_published = True
        post.save()
        
        subscribers = Subscription.objects.filter(author=post.author)
        for subscription in subscribers:
            Notification.objects.create(
                user=subscription.subscriber,
                post=post,
                message=f"{post.author.username} published: {post.title}"
            )
        
        published_count += 1
    
    return f"Published {published_count} posts"


@shared_task
def cleanup_old_notifications():
    """Clean up old notifications"""
    from datetime import timedelta
    cutoff_date = timezone.now() - timedelta(days=30)
    deleted_count = Notification.objects.filter(
        created_at__lt=cutoff_date,
        is_read=True
    ).delete()[0]
    
    return f"Deleted {deleted_count} old notifications" 