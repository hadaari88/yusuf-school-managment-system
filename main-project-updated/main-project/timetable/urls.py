from django.urls import path
from . import views

urlpatterns = [
    path('', views.timetable_list, name='timetable_list'),
    path('<int:pk>/', views.timetable_detail, name='timetable_detail'),
    path('<int:pk>/edit/', views.timetable_edit, name='timetable_edit'),
    path('<int:pk>/delete/', views.timetable_delete, name='timetable_delete'),
    path('add/', views.timetable_add, name='timetable_add'),
]
