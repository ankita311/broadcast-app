from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver


def post_upload_path(instance, filename):
    return f'posts/{instance.author.username}/{filename}'


class Profile(models.Model):
    ROLE_CHOICES = [
        ('resident', 'Resident'),
        ('rwa_member', 'RWA Member'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='resident')
    house_number = models.CharField(max_length=50, blank=False, null=False)
    building_number = models.CharField(max_length=50, blank=False, null=False)
    society = models.CharField(max_length=200, blank=False, null=False)
    
    def __str__(self):
        return f"Profile of {self.user.username} ({self.get_role_display()})"
    
    def is_rwa_member(self):
        return self.role == 'rwa_member'
    
    def is_resident(self):
        return self.role == 'resident'


class Post(models.Model):
    CATEGORY_CHOICES = [
        ('celebration', 'Celebration'),
        ('grievance', 'Grievance'),
        ('information', 'Information'),
        ('invitation', 'Invitation'),
        ('safety', 'Safety & Security'),
        ('maintenance', 'Maintenance'),
        ('event', 'Event'),
        ('announcement', 'Announcement'),
        ('complaint', 'Complaint'),
        ('suggestion', 'Suggestion'),
        ('emergency', 'Emergency'),
        ('lost_found', 'Lost & Found'),
        ('other', 'Other'),
    ]
    
    
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='information')
    image = models.ImageField(upload_to=post_upload_path, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    scheduled_for = models.DateTimeField()
    is_published = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.title} by {self.author.username}"


class Subscription(models.Model):
    subscriber = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscriptions')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscribers')
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ['subscriber', 'author']
    
    def __str__(self):
        return f"{self.subscriber.username} follows {self.author.username}"


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    message = models.CharField(max_length=500)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Notification for {self.user.username}: {self.message[:50]}"


# Signal to automatically create Profile when User is created
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
