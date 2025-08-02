from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from .models import Post, Subscription, Notification, Profile
from .forms import PostForm, UserRegistrationForm, ProfileForm
from django.contrib.auth.models import User



def home(request):
    posts = Post.objects.filter(is_published=True).order_by('-scheduled_for')
    
    subscription_status = {}
    if request.user.is_authenticated:
        for post in posts:
            if post.author != request.user:
                subscription_status[post.author.id] = Subscription.objects.filter(
                    subscriber=request.user, 
                    author=post.author
                ).exists()
    
    return render(request, 'website/home.html', {
        'posts': posts,
        'subscription_status': subscription_status
    })


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.save()
            profile = user.profile
            profile.house_number = form.cleaned_data.get('house_number', '')
            profile.building_number = form.cleaned_data.get('building_number', '')
            profile.society = form.cleaned_data.get('society', '')
            profile.save()
            
            login(request, user)
            messages.success(request, 'Account created successfully!')
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'website/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, 'Logged in successfully!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials!')
    return render(request, 'website/login.html')


@login_required
def user_logout(request):
    logout(request)
    messages.success(request, 'Logged out successfully!')
    return redirect('home')


@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, 'Post scheduled successfully!')
            return redirect('my_posts')
    else:
        form = PostForm()
    return render(request, 'website/create_post.html', {'form': form})


@login_required
def my_posts(request):
    posts = Post.objects.filter(author=request.user).order_by('-created_at')
    return render(request, 'website/my_posts.html', {'posts': posts})


@login_required
def subscribe(request, user_id):
    author = get_object_or_404(User, id=user_id)
    
    if author == request.user:
        messages.error(request, 'You cannot subscribe to yourself!')
        return redirect('home')
    
    subscription, created = Subscription.objects.get_or_create(
        subscriber=request.user,
        author=author
    )
    
    if created:
        messages.success(request, f'You are now following {author.username}!')
    else:
        messages.info(request, f'You are already following {author.username}!')
    
    return redirect('user_profile', user_id=user_id)


@login_required
def unsubscribe(request, user_id):
    author = get_object_or_404(User, id=user_id)
    
    try:
        subscription = Subscription.objects.get(subscriber=request.user, author=author)
        subscription.delete()
        messages.success(request, f'You unfollowed {author.username}!')
    except Subscription.DoesNotExist:
        messages.error(request, 'You were not following this user!')
    
    return redirect('user_profile', user_id=user_id)


@login_required
def user_profile(request, user_id):
    user = get_object_or_404(User, id=user_id)
    posts = Post.objects.filter(author=user, is_published=True).order_by('-scheduled_for')
    
    is_subscribed = False
    if request.user != user:
        is_subscribed = Subscription.objects.filter(subscriber=request.user, author=user).exists()
    
    return render(request, 'website/user_profile.html', {
        'profile_user': user,
        'posts': posts,
        'is_subscribed': is_subscribed
    })


@login_required
def notifications(request):
    notifications = Notification.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'website/notifications.html', {'notifications': notifications})


@login_required
def mark_notification_read(request, notification_id):
    notification = get_object_or_404(Notification, id=notification_id, user=request.user)
    notification.is_read = True
    notification.save()
    messages.success(request, 'Notification marked as read!')
    return redirect('notifications')


def publish_scheduled_posts():
    now = timezone.now()
    posts_to_publish = Post.objects.filter(
        scheduled_for__lte=now,
        is_published=False
    )
    
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


@login_required
def profile_edit(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('user_profile', user_id=request.user.id)
    else:
        form = ProfileForm(instance=request.user.profile)
    
    return render(request, 'website/profile_edit.html', {'form': form})
