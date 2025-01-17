from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Movie

class MovieListView(generic.ListView):
    model = Movie
    template_name = "movie/movie_list.html"
    context_object_name = "movies"
    queryset = Movie.objects.all().order_by("Year") # filter year from oldest to newest
    template_name = "movie/index.html"
    paginate_by = 6    

def post_detail(request, slug):

    queryset = Movie.objects.filter(Status=1)
    post = get_object_or_404(queryset, Slug=slug)
    return render(request, "movie/post_detail.html", {"Movie": post},)
    
    
