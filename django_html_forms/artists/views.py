from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.http import HttpResponseNotFound

from .models import Artist, Song


def artists(request):
    artists = Artist.objects.all()
    return render(request, 'index.html', context={'artists': artists})


def create_song(request):
    artist_id = request.POST['artist_id']
    title = request.POST['title']
    album_name = request.POST.get('album_name', '')

    # validate required fields
    if not artist_id or not title:
        return redirect('artists')

    try:
        artist = Artist.objects.get(id=artist_id)
    except Artist.DoesNotExist:
        return HttpResponseNotFound()

    Song.objects.create(artist=artist, title=title, album_name=album_name)
    return redirect('artists')


def delete_song(request):
    song_id = request.POST['song_id']
    try:
        song = Song.objects.get(id=song_id)
    except Artist.DoesNotExist:
        return HttpResponseNotFound()
    song.delete()
    return redirect('artists')


def create_artist(request):
    artistic_name = request.POST.get('artistic_name')
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    picture_url = request.POST.get('picture_url')
    popularity = request.POST.get('popularity')
    genre = request.POST.get('genre')
    
    if not artistic_name:
        return redirect('artists')

    Artist.objects.create(artistic_name=artistic_name, first_name=first_name, last_name=last_name, picture_url=picture_url,popularity=popularity, genre=genre)
    return redirect('artists')

def delete_artist(request):
    artist_id = request.POST.get('artist_id')
    get_object_or_404(Artist, id=artist_id).delete()
    return redirect('artists')

