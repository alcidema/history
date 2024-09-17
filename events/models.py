from django.db import models
from django.contrib.postgres.fields import ArrayField


class Event(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

    sources = ArrayField(models.IntegerField())

    public = models.BooleanField(default=False)
