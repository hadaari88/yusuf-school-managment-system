from django.urls import path
from .views import FeeListView, FeeCreateView, FeeUpdateView, FeeDeleteView

app_name = 'fees'

urlpatterns = [
    path('', FeeListView.as_view(), name='fee-list'),
    path('add/', FeeCreateView.as_view(), name='fee-add'),
    path('edit/<int:pk>/', FeeUpdateView.as_view(), name='fee-edit'),
    path('delete/<int:pk>/', FeeDeleteView.as_view(), name='fee-delete'),
]
