from django.db import models

class Score(models.Model):
    match = models.OneToOneField('matches.Match', on_delete=models.CASCADE)
    score_team1 = models.PositiveIntegerField()
    score_team2 = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.match} - {self.score_team1}:{self.score_team2}"
    
    class Meta:
        db_table = "scores"
