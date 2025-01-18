from . import views
from django.urls import path

urlpatterns = [
    path("", views.MovieListView.as_view(), name="home"),
    path('<slug:slug>/', views.post_detail, name="post_detail"),
 ##   path('movie/<int:movie_id>/add_comment/', views.add_comment, name='add_comment'),
]