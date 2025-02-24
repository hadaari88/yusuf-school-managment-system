# models.py
from django.db import models

class Department(models.Model):
    CATEGORY_CHOICES = (
        ('academic', 'Academic Departments'),
        ('arts', 'Arts & Creative Departments'),
        ('technical', 'Technical & Vocational Departments'),
        ('sports', 'Sports & Physical Education'),
        ('administrative', 'Administrative Departments'),
    )
    
    name = models.CharField(max_length=100, unique=True)  # Ensure department names are unique
    code = models.CharField(max_length=10, unique=True, blank=True, null=True)  # Optional department code
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)  # Set only on creation
    updated_at = models.DateTimeField(auto_now=True)      # Update on each save

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]  # Sorted alphabetically
        verbose_name_plural = "Departments"  # Correct plural in Django Admin
