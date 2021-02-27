from django.db import models
from django.utils.timezone import now


class ImageCollector(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=300)
    photo = models.ImageField(upload_to="pics")
    description = models.TextField()
    date = models.DateField(default=now)
