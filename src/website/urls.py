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
    path('subscribe/<int:user_id>/', views.subscribe, name='subscribe'),
    path('unsubscribe/<int:user_id>/', views.unsubscribe, name='unsubscribe'),
    path('notifications/', views.notifications, name='notifications'),
    path('mark-read/<int:notification_id>/', views.mark_notification_read, name='mark_notification_read'),
] 