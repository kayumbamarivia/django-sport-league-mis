from django.urls import path,include
from .views import register, user_login, user_logout,home, unauthorized_access, github_login

urlpatterns = [
    path('',home, name='home'),
    path('register/', register, name='register'),
    path('login/', user_login, name='user_login'),
    path('logout/', user_logout, name='user_logout'),
    path('accounts/', include('allauth.urls')),
    path('accounts/github/login/', github_login, name='github_login')
]
