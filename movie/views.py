from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def my_movie(request):
    return HttpResponse("This is going to be the most amazing movie website ever!")
