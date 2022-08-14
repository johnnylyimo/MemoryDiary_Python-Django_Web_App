from turtle import update
from django.db import models

class TrackingModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField()