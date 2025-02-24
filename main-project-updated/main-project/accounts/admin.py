from django.contrib import admin
from .models import FeePayment, Expense, SalaryPayment

admin.site.register(FeePayment)
admin.site.register(Expense)
admin.site.register(SalaryPayment)
