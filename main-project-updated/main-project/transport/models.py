from django.db import models

class Transport(models.Model):
    VEHICLE_CHOICES = [
        ('bus', 'Bus'),
        ('van', 'Van'),
        ('car', 'Car'),
        ('bike', 'Bike'),
    ]
    
    name = models.CharField(max_length=100)
    vehicle_type = models.CharField(max_length=20, choices=VEHICLE_CHOICES)
    registration_number = models.CharField(max_length=20)
    capacity = models.IntegerField(default=0)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} ({self.get_vehicle_type_display()})"
