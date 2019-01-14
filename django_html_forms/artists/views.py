from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseNotFound

from .models import Artist, Song


def artists(request):
    artists = Artist.objects.all()
    return render(request, 'index.html', context={'artists': artists})


def create_song(request):
    # Generally ,
    # is a way to fetch a value while providing a default if it does not exist.
    # my_var = dict.get(<key>, <default>)

    artist_id = request.POST.get('artist_id', False)
    title = request.POST.get('title', False)
    album_name = request.POST.get('album_name', False)

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
    if request.method == 'POST':
        artistic_name = request.POST['artistic_name']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        picture_url = request.POST['picture_url']
        popularity = request.POST['popularity']
        genre = request.POST.get('genre', False)

        if artistic_name and first_name and last_name and picture_url and popularity and genre:
            artist = Artist()
            artist.artistic_name = artistic_name
            artist.first_name = first_name
            artist.last_name = last_name
            artist.picture_url = picture_url
            artist.popularity = int(popularity)
            artist.genre = genre
            #   print(artist.genre)
            artist.save()
            return redirect('artists')
        return render(request, "index.html", {'error': 'All fields are Required'})
    return render(request, "index.html")


def delete_artist(request):
    artist_id = request.POST.get('artist_id', False)
    artist = get_object_or_404(Artist, id=artist_id)

    # confirm delete for POST request
    if request.method == 'POST':
        artist.delete()
        return redirect('artists')
    return render(request, "index.html")