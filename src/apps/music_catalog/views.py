"""
Модуль который отвечает за показ музыки пользователю
"""

import random
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from apps.main.service import get_base_context
from apps.music_catalog.forms import UploadMusic
from apps.music_catalog.services import save_music_upload
from apps.music_catalog.models import Authors, Favourite_tracks, Music
from apps.music_catalog.services import like_track
from logger import configure_logging
from apps.main.service import get_objects_form_db_by_id, get_filtred_objects, get_all_objects

logger = configure_logging()


def music_upload(request: HttpRequest) -> HttpResponse:
    """
    Страница для загрузки музыки
    """
    logger.info(f"Пользователь зашел на страницу загрузки музыки")
    context = get_base_context("Title", "")
    context["UploadForm"] = UploadMusic()
    if request.method == "POST":
        logger.info(f"Пользователь хочет сохранить музыку")
        save_music_upload(request)
    return render(request, "pages/upload_music_page.html", context)


def music_player(request: HttpRequest, music_id: int) -> HttpResponse:
    """
    Страница, которая проигрывает музыку с id=music_id
    :param music_id: id музыки
    """
    logger.info(f"Пользователь зашел на страницу проигрывания трек(id:{music_id}")
    context = get_base_context("Title", "")
    context["Music"] = get_objects_form_db_by_id(Music, id=music_id)
    return render(request, "pages/music_player.html", context)


def random_music(request: HttpRequest) -> HttpResponse:
    """
    Страница, которая показывает рандомную музыку
    """
    logger.info(f"Пользователь зашел на страницу рандомной музыки")
    context = get_base_context("Title", "")
    l = len(get_all_objects(Music))
    rand_music = random.randint(1, l)
    context["Music"] = get_objects_form_db_by_id(Music, id=rand_music)
    return render(request, "pages/music_player.html", context)


def music_catalog(request: HttpRequest) -> HttpResponse:
    """
    Страница, которая показывает всю музыку
    """
    logger.info(f"Пользователь зашел на страницу каталога музыки")
    context = get_base_context("Title", "Популярные треки")
    Musics = get_all_objects(Music)
    context["Musics"] = Musics
    context["Like_tracks"] = [
        track.Track_id for track in get_filtred_objects(Favourite_tracks, User_id=request.user.id)
    ]
    context["Len"] = len(Musics)
    return render(request, "pages/Music_catalog.html", context)


def author_catalog(request: HttpRequest, author_id) -> HttpResponse:
    """
    Страница, которая показывает треки автора
    :param author_id: id автора
    """
    logger.info(f"Пользователь зашел на страницу каталога музыки автора")
    context = get_base_context("Title", Authors.objects.get(id=author_id).Name)
    Musics = get_filtred_objects(Music, Author_id=author_id)
    context["Musics"] = Musics
    context["Like_tracks"] = [
        track.Track_id for track in get_filtred_objects(Favourite_tracks, User_id=request.user.id)
    ]
    context["Author_name"] = get_objects_form_db_by_id(Authors, id=author_id).Name
    context["Len"] = len(Musics)
    return render(request, "pages/Music_catalog.html", context)


def favourite_tracks(request: HttpRequest) -> HttpResponse:
    """
    Страница, которая показывает любимые треки пользователя
    """
    logger.info(f"Пользователь зашел на страницу люьимых треков")
    context = get_base_context("MusicForSoul", "Любимые композиции")
    Favourite_musics = get_filtred_objects(Favourite_tracks, User_id=request.user.id)
    Musics = []
    for music in Favourite_musics:
        Musics.append(get_objects_form_db_by_id(Music, id=music.Track_id))
    context["Musics"] = Musics
    context["Like_tracks"] = [
        track.Track_id for track in get_filtred_objects(Favourite_tracks, User_id=request.user.id)
    ]
    context["Len"] = len(Musics)
    return render(request, "pages/Music_catalog.html", context)


def service(request: HttpRequest):
    """
    Страница, которая обрабатывает запросы
    """
    context = get_base_context("MusicForSoul", "")
    like_track(request)
    return render(request, "pages/Music_catalog.html", context)
