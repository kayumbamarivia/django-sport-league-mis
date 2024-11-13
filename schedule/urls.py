from django.urls import path
from . import views

urlpatterns = [
    path('', views.schedule_list, name='schedule_list'),
    path('<int:pk>/', views.schedule_detail, name='schedule_detail'),
    path('add/', views.schedule_create, name='schedule_create'),
    path('<int:pk>/update/', views.schedule_update, name='schedule_update'),
    path('<int:pk>/delete/', views.schedule_delete, name='schedule_delete')
]
