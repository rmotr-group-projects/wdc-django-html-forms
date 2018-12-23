"""django_html_forms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from artists.views import (
    artists,
    create_song,
    delete_song,
    create_artist,
    delete_artist
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('artists/', artists, name='artists'),
    path('create-song/', create_song, name='create_song'),
    path('delete-song/', delete_song, name='delete_song'),
    path('create-artist/', create_artist, name="create_artist"),
    path('delete-artist/', delete_artist, name="delete_artist")
]
