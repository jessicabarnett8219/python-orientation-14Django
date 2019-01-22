from django.shortcuts import render

from django.http import HttpResponse

# from .models import Artist


def index(request):
    return HttpResponse("Hello, world. You're at the history index.")

def artist(request):
    # artist_list = Artist.objects.all()
    return HttpResponse("Hello, world. You're at the artists page.")

def detail(request, artist_id):
    return HttpResponse("You're looking at this artist: %s." % artist_id)