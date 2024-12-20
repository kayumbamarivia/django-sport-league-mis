from django.db import models
from leagues.models import League

class Report(models.Model):
    league = models.ForeignKey(League, on_delete=models.CASCADE)
    generated_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return f"Report for {self.league} - {self.generated_at}"
    
    class Meta:
        db_table = "reports"