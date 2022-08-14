from django.db import models
from helpers.models import TrackingModel

# Create your models here.

class Memory(TrackingModel):
    title = models.CharField(max_length=250)
    content = models.TextField()
