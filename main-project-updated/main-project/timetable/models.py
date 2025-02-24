from django.db import models

class Timetable(models.Model):
    day_of_week = models.CharField(max_length=20, choices=[
        ('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')
    ])
    subject = models.ForeignKey('subjects.Subject', on_delete=models.CASCADE)
    teacher = models.ForeignKey('teachers.Teacher', on_delete=models.CASCADE)
    start_time = models.TimeField()
    end_time = models.TimeField()
    classroom = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.subject} - {self.day_of_week} ({self.start_time} - {self.end_time})"
