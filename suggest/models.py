from django.db import models

# Create your models here.

class QueryLog(models.Model):
    query = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    tone = models.CharField(max_length=100)
    intent = models.CharField(max_length=100)
    suggestions = models.JSONField()

    def __str__(self):
        return f"QueryLog({self.queryText[:20]}...)"
