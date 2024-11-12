from django.db import models

class League(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    teams = models.ManyToManyField('teams.Team')

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "leagues"