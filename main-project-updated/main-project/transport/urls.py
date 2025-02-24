from django.urls import path
from .views import transport_list, transport_create, transport_update, transport_delete

urlpatterns = [
    path('', transport_list, name='transport_list'),
    path('new/', transport_create, name='transport_create'),
    path('<int:pk>/edit/', transport_update, name='transport_update'),
    path('<int:pk>/delete/', transport_delete, name='transport_delete'),
]
