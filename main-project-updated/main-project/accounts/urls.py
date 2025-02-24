from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    # Fee Payment URLs
    path('fees/', views.fee_list, name='fee_list'),
    path('fees/<int:pk>/', views.fee_detail, name='fee_detail'),
    path('fees/add/', views.add_fee_payment, name='add_fee_payment'),
    path('fees/<int:pk>/edit/', views.edit_fee_payment, name='edit_fee_payment'),
    path('fees/<int:pk>/delete/', views.delete_fee_payment, name='delete_fee_payment'),
    # Salary Payment URLs
    path('salary/summary/', views.salary, name='salary'),
    #  path('salary/', views.salary_list, name='salary_list'),
    path('salary/<int:pk>/', views.salary_detail, name='salary_detail'),
    path('salary/add/', views.add_salary_payment, name='add_salary_payment'),
    path('salary/<int:pk>/edit/', views.edit_salary_payment, name='edit_salary_payment'),
    path('salary/<int:pk>/delete/', views.delete_salary_payment, name='delete_salary_payment'),
    # Expense URLs
    path('expenses/', views.expenses, name='expenses'),  # This is the missing URL
    path('expenses/<int:pk>/', views.expense_detail, name='expense_detail'),
    path('expenses/add/', views.add_expense, name='add_expense'),
    path('expenses/<int:pk>/edit/', views.edit_expense, name='edit_expense'),
    path('expenses/<int:pk>/delete/', views.delete_expense, name='delete_expense'),
    # Fees collection (if needed)
    path('fees/collection/', views.fees_collection, name='fees_collection'),
]
