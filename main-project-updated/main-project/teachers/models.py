from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.db.models.signals import pre_save

class Teacher(models.Model):
    DEPARTMENT_CHOICES = [
        ('Computer Science', 'Computer Science'),
        ('Mathematics', 'Mathematics'),
        ('Physics', 'Physics'),
    ]

    # Optional: link to a user account (set null/blank as needed)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    department = models.CharField(max_length=50, choices=DEPARTMENT_CHOICES, default='Computer Science')
    profile_image = models.ImageField(upload_to='teachers/', null=True, blank=True)
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

def pre_save_teacher_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(f"{instance.first_name}-{instance.last_name}")

pre_save.connect(pre_save_teacher_receiver, sender=Teacher)
