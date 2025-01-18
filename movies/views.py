from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Movie, Comment
from .models import Comment
from django.urls import path
from . import views
from .forms import CommentForm


class MovieListView(generic.ListView):
    model = Movie
    template_name = "movie/movie_list.html"
    context_object_name = "movies"
    queryset = Movie.objects.all().order_by("year") # filter year from oldest to newest
    template_name = "movie/index.html"
    paginate_by = 6    

def post_detail(request, slug):

    post = get_object_or_404(Movie, slug=slug)
    return render(request, "movie/post_detail.html", {"movie": post})
    
    
#added this to allow users to add comments to a movie
