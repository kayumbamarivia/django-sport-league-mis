from django.db import models
from users.models import User

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    coach = models.ForeignKey(User,limit_choices_to={'role': 'coach'}, on_delete=models.SET_NULL, null=True, blank=True)
    players = models.TextField()

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "teams"
