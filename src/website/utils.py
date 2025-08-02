from .models import Notification

def get_unread_notifications_count(request):
    """Get unread notifications count for context processor"""
    if request.user.is_authenticated:
        return Notification.objects.filter(user=request.user, is_read=False).count()
    return 0

def unread_notifications(request):
    """Context processor to provide unread notifications count"""
    return {'unread_notifications_count': get_unread_notifications_count(request)} 