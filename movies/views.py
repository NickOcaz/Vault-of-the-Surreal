from django.shortcuts import render
from django.views import generic
from .models import Movie

class MovieListView(generic.ListView):
    model = Movie
##    template_name = "movie/movie_list.html"
##    context_object_name = "movies"
    queryset = Movie.objects.all().order_by("Year") # filter year from oldest to newest
    template_name = "movie/index.html"
#    context_object_name = "movies"
    paginate_by = 12    

    
    
    
