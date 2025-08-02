from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('create-post/', views.create_post, name='create_post'),
    path('my-posts/', views.my_posts, name='my_posts'),
    path('profile/<int:user_id>/', views.user_profile, name='user_profile'),
    path('profile/edit/', views.profile_edit, name='profile_edit'),
    path('subscribe/<int:user_id>/', views.subscribe, name='subscribe'),
    path('unsubscribe/<int:user_id>/', views.unsubscribe, name='unsubscribe'),
    path('notifications/', views.notifications, name='notifications'),
    path('mark-read/<int:notification_id>/', views.mark_notification_read, name='mark_notification_read'),
    path('update-post/<int:post_id>/', views.update_post, name='update_post'),
    path('delete-post/<int:post_id>/', views.delete_post, name='delete_post'),
    # RWA Member specific URLs
    path('community-management/', views.community_management, name='community_management'),
    path('mark-resolved/<int:post_id>/', views.mark_grievance_resolved, name='mark_grievance_resolved'),
    # Public RWA Dashboard
    path('rwa-members/', views.public_rwa_dashboard, name='public_rwa_dashboard'),
] 