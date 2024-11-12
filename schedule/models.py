from django.db import models

class Schedule(models.Model):
    match = models.OneToOneField('matches.Match', on_delete=models.CASCADE)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"Schedule for {self.match}"
    
    class Meta:
        db_table = "schedule"
