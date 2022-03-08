from django.db import models
from django.utils import timezone

# Create your models here.
class todo(models.Model):
    title = models.CharField(max_length = 100)
    description = models.CharField(max_length=100)
    date=models.DateTimeField(default=timezone.now)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title