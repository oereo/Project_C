from django.db import models
from account.models import User

class Area(models.Model):
    areaUser = models.ForeignKey('account.User', on_delete=models.CASCADE, related_name='areaUser')
    measuringInstrument = models.CharField(max_length=200)
    text = models.TextField()

    def __str__(self):
        return self.text

class Profile(models.Model):
    user = models.OneToOneField('account.User', on_delete=models.CASCADE, related_name='profileUser')
    worker_number = models.TextField(max_length=500, blank=True)
    instrument_number = models.CharField(max_length=30, blank=True)
    safe_percent = models.CharField(max_length = 30 ,null=True, blank=True)

class Instrument(models.Model):
    instrument = models.CharField(max_length = 30)

    def __str__(self):
        return self.instrument
