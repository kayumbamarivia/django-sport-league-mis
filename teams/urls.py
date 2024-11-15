from django.urls import path
from . import views

urlpatterns = [
    path('', views.team_list, name='team_list'),
    path('add/', views.team_create, name='team_create'),
    path('<int:pk>/edit/', views.team_update, name='team_update'),
    path('<int:pk>/delete/', views.team_delete, name='team_delete'),
    path('<int:pk>/players/', views.team_players, name='team_players'),
]
