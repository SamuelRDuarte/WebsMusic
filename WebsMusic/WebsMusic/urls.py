"""WebsMusic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('home/', views.home, name='home'),
    path('artistas/', views.artistas, name='artistas'),
    path('musicas/', views.musicas, name='musicas'),
    path('criarPlayList/', views.criarPlayList, name='criarPlayList'),
    path('artistTracks/', views.artist_tracks, name='artistTracks'),
    path('albums/', views.albums, name='albums'),
    path('albumDetails/', views.albumInfo, name='albumDetails'),
    path('myPlayList/', views.myPlayList, name='myPlayList'),
    #path('pageRSS/', views.pageRSS, name='pageRSS'),
    path('delete/', views.delete, name='delete'),
    path('knowArtists/', views.knowArtists, name='knowArtists'),
    path('Recommendations/', views.Recommendations, name='Recommendations'),

]
