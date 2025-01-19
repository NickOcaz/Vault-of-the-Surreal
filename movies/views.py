from django.shortcuts import render, get_object_or_404, reverse
from django.contrib import messages
from django.urls import reverse
from django.views import generic
from django.http import HttpResponseRedirect
from django.db.models import Count  # Import Count
from .models import Movie, Comment
from django.urls import path
from . import views
from .forms import CommentForm

#movie details

class MovieListView(generic.ListView):
    model = Movie
    template_name = "movie/movie_list.html"
    context_object_name = "movies"
    queryset = Movie.objects.all().annotate(comment_count=Count('comments')).order_by("year") # filter year from oldest to newest
    template_name = "movie/index.html"
    paginate_by = 6    


# submit comments

def post_detail(request, slug):

    queryset = Movie.objects.filter(status=1)
    post = get_object_or_404(Movie, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.movie = post
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )

    comment_form = CommentForm()
    
    return render(
        request,
        "movie/post_detail.html",
        {
            "movie": post,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        },
    )

#edit comment
    
def comment_edit(request, slug, comment_id):

    if request.method == "POST":
    
        queryset = Movie.objects.filter(status=1)
        post = get_object_or_404(Movie, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))

#delete comment

def comment_delete(request, slug, comment_id):
    
    queryset = Movie.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))
