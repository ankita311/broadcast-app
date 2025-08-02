from django.core.management.base import BaseCommand
from website.models import Profile


class Command(BaseCommand):
    help = 'Remove all profile records from the database'

    def add_arguments(self, parser):
        parser.add_argument(
            '--confirm',
            action='store_true',
            help='Confirm that you want to delete all profiles',
        )

    def handle(self, *args, **options):
        if not options['confirm']:
            self.stdout.write(
                self.style.WARNING(
                    'This will delete ALL profile records from the database!\n'
                    'Run with --confirm to proceed.'
                )
            )
            return

        profile_count = Profile.objects.count()
        Profile.objects.all().delete()
        
        self.stdout.write(
            self.style.SUCCESS(
                f'Successfully deleted {profile_count} profile records from the database.'
            )
        ) 