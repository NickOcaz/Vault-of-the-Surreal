from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


STATUS = ((0, "Draft"), (1, "Published"))

class Movie(models.Model):
    movieID = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=200, unique=True)
    year = models.IntegerField(null=True, blank=True)
    director = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    featured_image = CloudinaryField('image', default='placeholder')
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ["-year"]

    def __str__(self):
        return f"{self.title} | Directed by {self.director} | year {self.year}"
        
class Comment(models.Model):
    movie = models.ForeignKey(
        Movie, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.author}"
