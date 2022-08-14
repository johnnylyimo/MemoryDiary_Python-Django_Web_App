from django.db import models
from helpers.models import TrackingModel

# Create your models here.

class Memory(TrackingModel):
    title = models.CharField(max_length=250)
    content = models.TextField()

    def __str__(self):
        return self.title if self.title != "" else self.content[0:len(self.content)]
