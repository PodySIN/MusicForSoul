"""
Модуль отвечающий за url для показа музыки
"""

from django.urls import path
from apps.music_catalog import views

urlpatterns = [
    path("upload_music/", views.music_upload, name="UploadMusic"),
    path("music_catalog/", views.music_catalog, name="MusicCatalog"),
    path(
        "music_catalog/PlayMusic/<int:music_id>",
        views.music_player,
        name="Cur_music",
    ),
    path("random_music/", views.random_music, name="RandomMusic"),
    path(
        "music_catalog/Author/<int:author_id>/",
        views.author_catalog,
        name="Cur_author",
    ),
    path(
        "music_catalog/Favourite_tracks/",
        views.favourite_tracks,
        name="Favourite_tracks",
    ),
    path("service/", views.service, name="like_track"),
]
