from django.db import models

class Match(models.Model):
    team1 = models.ForeignKey('teams.Team', related_name='home_matches', on_delete=models.CASCADE)
    team2 = models.ForeignKey('teams.Team', related_name='away_matches', on_delete=models.CASCADE)
    date = models.DateTimeField()
    venue = models.CharField(max_length=100)
    league = models.ForeignKey('leagues.League', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.team1} vs {self.team2} - {self.date.strftime('%Y-%m-%d')}"
    
    class Meta:
        db_table = "matches"