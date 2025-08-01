from django.core.management.base import BaseCommand
from django_celery_beat.models import PeriodicTask, CrontabSchedule
from website.tasks import publish_scheduled_posts_task


class Command(BaseCommand):
    help = 'Set up periodic task for publishing scheduled posts'

    def handle(self, *args, **options):
        # Create a schedule that runs every minute
        schedule, created = CrontabSchedule.objects.get_or_create(
            minute='*',
            hour='*',
            day_of_week='*',
            day_of_month='*',
            month_of_year='*',
        )
        
        if created:
            self.stdout.write('Created crontab schedule')
        
        # Create the periodic task
        task, created = PeriodicTask.objects.get_or_create(
            name='Publish Scheduled Posts',
            defaults={
                'task': 'website.tasks.publish_scheduled_posts_task',
                'crontab': schedule,
                'enabled': True,
            }
        )
        
        if created:
            self.stdout.write(self.style.SUCCESS('Successfully created periodic task for publishing posts'))
        else:
            self.stdout.write('Periodic task already exists') 