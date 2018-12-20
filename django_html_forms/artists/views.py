from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound

from .models import Artist, Song


def artists(request):
    artists = Artist.objects.all()
    
    artist_first_name_filter = request.GET.get('first_name')
    popularity_filter = request.GET.get('popularity')
    
    if artist_first_name_filter:
        artists = artists.filter(first_name__icontains=artist_first_name_filter)
    
    if popularity_filter:
        artists = artists.filter(popularity__gte=popularity_filter)
        
    return render(request, 'artists.html', context={'artists': artists})

def artist(request, artist_id):
    artist = Artist.objects.get(id=artist_id)
    return render(request, 'artist.html', context={'artist': artist})
    
def list_songs(request):
    all_artists = Artist.objects.all()
    all_artist_set = None
    
    title_filter = request.GET.get('title')
    if title_filter:
        all_artist_set = []
        for artist in all_artists:
            all_songs = artist.song_set.filter(title__icontains=title_filter)
            for song in all_songs:
                if song.artist not in all_artist_set:
                    all_artist_set.append(song.artist)
    
    if all_artist_set:
        context={'artists': all_artist_set}
    else:
        context={'artists': all_artists}
    return render(request, 'artist_songs.html', context=context)


def artist_songs(request, artist_id):
    artist = Artist.objects.get(id=artist_id)
    return render(request, 'artist_songs.html', context={'artists': [artist]})

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
    pass


def delete_artist(request):
    pass
