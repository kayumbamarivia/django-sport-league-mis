from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from allauth.socialaccount.providers.github.views import GitHubOAuth2Adapter
from allauth.socialaccount.providers.oauth2.views import OAuth2Adapter
from allauth.socialaccount.models import SocialAccount

# Function to handle unauthorized access
def unauthorized_access(request, exception):
    return render(request, 'unauthorized.html', status=404)

# Function for the home view
def home(request):
    if request.user.is_authenticated:
        logout(request)
    return render(request, 'home.html')

# Function to handle user registration
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            print(f"User {user.username} created successfully!")
            login(request, user)
            return redirect('team_list') 
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})

# Function to handle user login
def user_login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('team_list') 
    else:
        form = CustomAuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

# Custom GitHub login view to redirect to the desired URL
def github_login(request):
    if request.user.is_authenticated:
        return redirect('team_list') 
    else:
        return redirect('account_login')

# Function for user logout
def user_logout(request):
    logout(request)
    return redirect('user_login')
