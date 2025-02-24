from django.urls import path
from .views import sports_list, sport_create, sport_update, sport_delete

urlpatterns = [
    path('', sports_list, name='sports_list'),
    path('new/', sport_create, name='sport_create'),
    path('<int:pk>/edit/', sport_update, name='sport_update'),
    path('<int:pk>/delete/', sport_delete, name='sport_delete'),
]
