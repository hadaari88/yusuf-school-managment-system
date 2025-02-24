from django.urls import path
from . import views

urlpatterns = [
    path('', views.teacher_list, name='teacher_list'),
    path('add/', views.add_teacher, name='add_teacher'),
    path('dashboard/<slug:slug>/', views.teacher_dashboard, name='teacher_dashboard'),
    
    path('<slug:slug>/', views.view_teacher, name='view_teacher'),
    path('edit/<slug:slug>/', views.edit_teacher, name='edit_teacher'),
    path('delete/<slug:slug>/', views.delete_teacher, name='delete_teacher'),
    
]
