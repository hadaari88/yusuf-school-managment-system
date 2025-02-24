from django.urls import path
from . import views

urlpatterns = [
    path('', views.subject_list, name='subject_list'),
    path('dashboard/', views.subject_dashboard, name='subject_dashboard'),
    path('add/', views.add_subject, name='add_subject'),
    path('<int:pk>/', views.view_subject, name='view_subject'),
    path('<int:pk>/edit/', views.edit_subject, name='edit_subject'),
    path('<int:pk>/delete/', views.delete_subject, name='delete_subject'),
]
