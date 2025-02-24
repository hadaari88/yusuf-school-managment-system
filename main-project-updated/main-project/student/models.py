from django.db import models
from django.utils.text import slugify
from django.utils.crypto import get_random_string

class Parent(models.Model):
    father_name = models.CharField(max_length=100)
    father_occupation = models.CharField(max_length=100, blank=True)
    father_mobile = models.CharField(max_length=15)
    father_email = models.EmailField(max_length=100)
    mother_name = models.CharField(max_length=100)
    mother_occupation = models.CharField(max_length=100, blank=True)
    mother_mobile = models.CharField(max_length=15)
    mother_email = models.EmailField(max_length=100)
    present_address = models.TextField()
    permanent_address = models.TextField()

    def __str__(self):
        return f"{self.father_name} & {self.mother_name}"

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=20, unique=True)  
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')])
    date_of_birth = models.DateField()
    student_class = models.CharField(max_length=50)
    religion = models.CharField(max_length=50)
    joining_date = models.DateField()
    mobile_number = models.CharField(max_length=15)
    admission_number = models.CharField(max_length=20, unique=True)  
    section = models.CharField(max_length=10)
    student_image = models.ImageField(upload_to='students/', blank=True)
    parent = models.OneToOneField(Parent, on_delete=models.CASCADE)

    # Ensure these fields have default values to avoid 'None'
    age = models.IntegerField(null=True, blank=True, default=18)  
    marks = models.IntegerField(null=True, blank=True, default=0)  
    fees = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, default=0.00)  

    slug = models.SlugField(max_length=255, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            clean_student_id = self.student_id.replace("/", "-")  
            base_slug = slugify(f"{self.first_name}-{self.last_name}-{clean_student_id}")
            self.slug = f"{base_slug}-{get_random_string(6)}"
        super(Student, self).save(*args, **kwargs)

    def __str__(self):
       return f"{self.first_name} {self.last_name} ({self.student_id})"
