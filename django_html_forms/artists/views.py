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
    fields = ['artistic_name', 'first_name', 'last_name', 'picture_url',
			'popularity', 'genre']
    artist_data = {field:request.POST.get(field,'') for field in fields}
    if not artist_data['artistic_name']:
        return redirect('artists')
	
    if not artist_data['popularity']:
        artist_data['popularity'] = 0 if not artist_data['popularity'] else int(artist_data['popularity']) 
		
    Artist.objects.create(**artist_data)
    return redirect('artists')


def delete_artist(request):
    artist_id = request.POST.get('artist_id')
    try:
        artist = Artist.objects.get(id=artist_id)
    except Artist.DoesNotExist:
        return HttpResponseNotFound()
    artist.delete()
    return redirect('artists')
