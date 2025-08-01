from django.core.management.base import BaseCommand
from website.views import publish_scheduled_posts


class Command(BaseCommand):
    help = 'Publish scheduled posts and send notifications'

    def handle(self, *args, **options):
        self.stdout.write('Publishing scheduled posts...')
        publish_scheduled_posts()
        self.stdout.write(self.style.SUCCESS('Successfully published scheduled posts')) 