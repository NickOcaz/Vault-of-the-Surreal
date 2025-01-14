from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("accounts/", include("allauth.urls")),
    path("", include("movies.urls"), name="movie-urls"),
    path('admin/', admin.site.urls),
]