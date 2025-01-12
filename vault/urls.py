from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include("movies.urls"), name="movie-urls"),
    path('admin/', admin.site.urls),
]