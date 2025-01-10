from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Movie(models.Model):
    movie_id = models.AutoField(primary_key=True)
    slug = models.SlugField(max_length=200, unique=True)
    title = models.CharField(max_length=255, unique=True)
    year = models.IntegerField(null=True, blank=True)
    director = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.title