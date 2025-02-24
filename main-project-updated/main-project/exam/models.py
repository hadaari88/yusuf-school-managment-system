from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save

class Exam(models.Model):
    EXAM_TYPE_CHOICES = [
        ('Midterm', 'Midterm'),
        ('Final', 'Final'),
        ('Quiz', 'Quiz'),
        ('Test', 'Test'),
    ]
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    exam_type = models.CharField(max_length=20, choices=EXAM_TYPE_CHOICES, default='Test')
    date = models.DateField()
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.name

def pre_save_exam_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.name)
        
pre_save.connect(pre_save_exam_receiver, sender=Exam)
