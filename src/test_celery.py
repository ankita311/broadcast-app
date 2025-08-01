#!/usr/bin/env python
import os
import django

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'broadcast.settings')
django.setup()

from website.tasks import publish_scheduled_posts_task
from celery import current_app

def test_celery():
    print("Testing Celery setup...")
    
    # Check if Celery app is configured
    print(f"Celery app: {current_app}")
    
    # Test the task directly
    try:
        result = publish_scheduled_posts_task.delay()
        print(f"Task submitted: {result}")
        print(f"Task ID: {result.id}")
        
        # Wait for result
        task_result = result.get(timeout=10)
        print(f"Task result: {task_result}")
        
    except Exception as e:
        print(f"Error running task: {e}")

if __name__ == "__main__":
    test_celery() 