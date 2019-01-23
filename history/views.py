from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Artist, Song, SongArtist

# request contains the information we need from the forms

def index(request):
  artist_list = Artist.objects.all()
  context = {'artist_list': artist_list}
  return render(request, 'history/index.html', context)


def detail(request, artist_id):
    artist = Artist.objects.get(pk=artist_id)
    # student_list = Student.objects.filter(cohort_id=cohort_id)
    song_list = SongArtist.objects.filter(artist_id=artist_id)
    context = {'song_list': song_list, 'artist': artist}
    return render(request, 'history/detail.html', context)