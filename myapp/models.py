from django.db import models
from django.urls import reverse

# Create your models here.


class Movie(models.Model):
    title = models.CharField(max_length=256)
    poster = models.CharField(max_length=1000)
    director = models.CharField(max_length=256)
    year = models.IntegerField(blank=True, null=True)

    def __str__ (self):
        return self.title
    def get_absolute_url(self):
        return reverse('main')




