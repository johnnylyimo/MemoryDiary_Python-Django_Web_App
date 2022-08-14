from django.db import models

class TrackingModel(models.Model):
    created_at = models.DateTimeField()