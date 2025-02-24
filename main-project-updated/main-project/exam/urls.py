from django.urls import path
from . import views

urlpatterns = [
    path('', views.exam_list, name='exam_list'),
    path('add/', views.add_exam, name='add_exam'),
    path('<slug:slug>/', views.exam_detail, name='exam_detail'),
    path('edit/<slug:slug>/', views.edit_exam, name='edit_exam'),
    path('delete/<slug:slug>/', views.delete_exam, name='delete_exam'),
]
