from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Post, Profile


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter first name'
    }))
    last_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter last name'
    }))
    house_number = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter house number'
    }))
    building_number = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter building number'
    }))
    society = forms.CharField(max_length=200, required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter society name'
    }))
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'house_number', 'building_number', 'society']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }


class PostForm(forms.ModelForm):
    scheduled_for = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        help_text='When should this post be published?'
    )
    
    class Meta:
        model = Post
        fields = ['title', 'content', 'image', 'scheduled_for']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'scheduled_for': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        } 


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['house_number', 'building_number', 'society']
        widgets = {
            'house_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter house number'}),
            'building_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter building number'}),
            'society': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter society name'}),
        } 