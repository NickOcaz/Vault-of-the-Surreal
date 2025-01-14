from django.db import models
from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))

class Movie(models.Model):
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
    
class Comment(models.Model):
    movie = models.ForeignKey(
        Movie, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    
    
