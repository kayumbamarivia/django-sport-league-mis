from django.urls import path
from . import views

urlpatterns = [
    # Matches
    path('', views.match_list, name='match_list'),
    path('<int:pk>/', views.match_detail, name='match_detail'),
    path('add/', views.match_create, name='match_create'),
    path('<int:pk>/update/', views.match_update, name='match_update'),
    path('<int:pk>/delete/', views.match_delete, name='match_delete')
]
