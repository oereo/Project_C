from django.db import models
from account.models import User

class Area(models.Model):
    areaUser = models.ForeignKey('account.User', on_delete=models.CASCADE, related_name='areaUser')
    measuringInstrument = models.CharField(max_length=200)
    text = models.TextField()

    def __str__(self):
        return self.text