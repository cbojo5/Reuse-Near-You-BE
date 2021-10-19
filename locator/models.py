from django.db import models

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=250)
    address = models.TextField()
    items_accepted = models.TextField(default='')
    latitude = models.FloatField()
    longitude = models.FloatField()