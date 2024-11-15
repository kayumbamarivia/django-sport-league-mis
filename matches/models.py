# matches/models.py
from django.db import models
from leagues.models import League
from teams.models import Team 

class Match(models.Model):
    team1 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team1_matches')
    team2 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team2_matches')
    date = models.DateTimeField()
    venue = models.CharField(max_length=200)
    league = models.ForeignKey(League, on_delete=models.CASCADE)
    score_team1 = models.IntegerField(default=0)
    score_team2 = models.IntegerField(default=0)

    STATUS_CHOICES = [
        ('scheduled', 'Scheduled'),
        ('ongoing', 'Ongoing'),
        ('completed', 'Completed'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='scheduled')

    def __str__(self):
        return f"{self.team1} vs {self.team2} at {self.venue} on {self.date}"
