from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Movie, Comment, Rating
from .forms import CommentForm, RatingForm
from django.db.models import Count, Avg

class MovieListView(generic.ListView):
    model = Movie
    template_name = "movie/index.html"
    context_object_name = "movies"
    queryset = Movie.objects.filter(status=1).annotate(
        comment_count=Count('comments'),
        average_rating=Avg('ratings__score')
    ).order_by("year")
    paginate_by = 6    

def post_detail(request, slug):
    queryset = Movie.objects.filter(status=1)
    movie = get_object_or_404(Movie, slug=slug)
    comments = movie.comments.order_by('-created_on')
    comment_count = comments.count()
    rating_form = RatingForm()
    user_rating = None

    if request.user.is_authenticated:
        user_rating = Rating.objects.filter(movie=movie, user=request.user).first()

    if request.method == "POST":
        if 'comment_form' in request.POST:
            comment_form = CommentForm(data=request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.author = request.user
                comment.movie = movie
                comment.save()
                messages.add_message(request, messages.SUCCESS, 'Comment submitted and awaiting approval')
                return redirect('post_detail', slug=slug)
        elif 'rating_form' in request.POST:
            rating_form = RatingForm(data=request.POST)
            if rating_form.is_valid():
                rating = rating_form.save(commit=False)
                rating.user = request.user
                rating.movie = movie
                existing_rating = Rating.objects.filter(movie=movie, user=request.user).first()
                if existing_rating:
                    existing_rating.score = rating.score
                    existing_rating.save()
                    messages.add_message(request, messages.SUCCESS, 'Rating updated')
                else:
                    rating.save()
                    messages.add_message(request, messages.SUCCESS, 'Rating submitted')
                return redirect('post_detail', slug=slug)

    comment_form = CommentForm()

    return render(request, "movie/post_detail.html", {
        "movie": movie,
        "comments": comments,
        "comment_count": comment_count,
        "comment_form": comment_form,
        "rating_form": rating_form,
        "user_rating": user_rating,
        "average_rating": movie.average_rating(),
    })

def comment_edit(request, slug, comment_id):
    queryset = Movie.objects.filter(status=1)
    movie = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST, instance=comment)
        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.movie = movie
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment updated and awaiting approval')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment')
    else:
        comment_form = CommentForm(instance=comment)
    return render(request, "movie/post_detail.html", {
        "movie": movie,
        "comments": movie.comments.order_by('-created_on'),
        "comment_count": movie.comments.count(),
        "comment_form": comment_form,
        "rating_form": RatingForm(),
        "user_rating": Rating.objects.filter(movie=movie, user=request.user).first(),
        "average_rating": movie.average_rating(),
    })

def comment_delete(request, slug, comment_id):
    queryset = Movie.objects.filter(status=1)
    movie = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)
    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments')
    return HttpResponseRedirect(reverse('post_detail', args=[slug]))