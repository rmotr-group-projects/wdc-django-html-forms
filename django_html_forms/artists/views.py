from django.shortcuts import render, redirect
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
    # django forms are far better. Manual forms suck. But to stay in constraints of the task...
    artistic_name = request.POST['artistic_name']
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    picture_url = request.POST['picture_url']
    popularity = int(request.POST['popularity'])
    genre = request.POST['genre']
    
    if not artistic_name or not first_name or not last_name or not picture_url or not popularity or not genre:
        return redirect('artists')

    new_artist = Artist.objects.create(artistic_name=artistic_name,
                                       first_name=first_name,
                                       last_name=last_name,
                                       picture_url=picture_url,
                                       popularity=popularity,
                                       genre=genre)
    return redirect('artists')


def delete_artist(request, artist_id):
    artist = Artist.objects.get(id=artist_id)
    artist.delete()
    return redirect('artists')
