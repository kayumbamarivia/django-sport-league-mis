from django.urls import path
from . import views

urlpatterns = [
    path('', views.score_list, name='score_list'),
    path('<int:pk>/', views.score_detail, name='score_detail'),
    path('add/', views.score_create, name='score_create'),
    path('<int:pk>/update/', views.score_update, name='score_update'),
    path('<int:pk>/delete/', views.score_delete, name='score_delete')
]
