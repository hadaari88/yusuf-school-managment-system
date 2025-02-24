from django.db import models

class League(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Sport(models.Model):
    LEAGUE_CHOICES = [
        ('champions_league', 'Champions League'),
        ('premier_league', 'Premier League'),
        ('final', 'Final'),
        ('friendly_game', 'Friendly Game'),
    ]
    
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    league = models.CharField(max_length=50, choices=LEAGUE_CHOICES)

    def __str__(self):
        return f"{self.name} - {self.get_league_display()}"

