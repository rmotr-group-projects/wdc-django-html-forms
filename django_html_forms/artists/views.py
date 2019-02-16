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
    # Django automatically creates an id field as primary key.
    # https://stackoverflow.com/questions/4300365/django-database-query-how-to-get-object-by-id
    if not artist_id or not title:
        return redirect('artists')

    # create ID is trying to find the artist ID (which exists if the object exists)
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
    
    # raises a key error if the key is not in the dictionary (POST['key'])
    artistic_name = request.POST['artistic_name']
    
    first_name = request.POST.get('first_name', '')
    last_name = request.POST.get('last_name', '')
    picture_url = request.POST.get('picture_url', '')
    popularity = request.POST.get('popularity', 0)    # WHY ZERO?
    genre = request.POST.get('genre', '')
    
    #validate inside the view that all the model's required fields have been sent from the template form
    #not clear why this was the only part required
    if not artistic_name:
        return redirect('artists')

    #convert popularity from a string to an integer value
    popularity = int(popularity)

    # create and save an object in a single step
    Artist.objects.create(
        artistic_name=artistic_name,
        first_name=first_name,
        last_name=last_name,
        picture_url=picture_url,
        popularity=popularity,
        genre=genre
    )
    return redirect('artists')

def delete_artist(request):
    artist_id = request.POST['artist_id']
    try:
        artist = Artist.objects.get(id=artist_id)
    except Artist.DoesNotExist:
        return HttpResponseNotFound()
    artist.delete()
    return redirect('artists')
