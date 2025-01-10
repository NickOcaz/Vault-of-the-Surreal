from django.db import models
from django.db import models

STATUS = ((0, "Draft"), (1, "Published"))

class Post(models.Model):
    MovieID = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=200, unique=True)
    Year = models.IntegerField(null=True, blank=True)
    Director = models.CharField(max_length=255, null=True, blank=True)
    Description = models.TextField(null=True, blank=True)
    ImageURL = models.CharField(max_length=255, null=True, blank=True)
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return self.Title