# admin.py
from django.contrib import admin
from .models import Department

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'category', 'description', 'created_at', 'updated_at')
    search_fields = ('name', 'code', 'category')
    list_filter = ('created_at', 'updated_at', 'category')

