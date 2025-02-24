# department/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.department_list, name='department_list'),
    path('category/<str:category>/', views.department_by_category, name='department_by_category'),
    path('<int:pk>/', views.department_detail, name='department_detail'),
    path('new/', views.department_create, name='department_create'),
    path('<int:pk>/edit/', views.department_edit, name='department_edit'),
    path('<int:pk>/delete/', views.department_delete, name='department_delete'),
    path('dashboard/', views.department_dashboard, name='department_dashboard'),
    path('code/<str:code>/', views.department_by_code, name='department_by_code'),
]
