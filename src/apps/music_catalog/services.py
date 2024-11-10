"""
Модуль который отвечает обработку данных, исходящих из модуля с показом страниц с музыкой
"""

from core.settings import BASE_DIR
from apps.music_catalog.forms import UploadMusic
from apps.music_catalog.models import Music
from apps.music_catalog.models import Authors
from django.http import HttpRequest, HttpResponse
from apps.music_catalog.models import Favourite_tracks
from logger import configure_logging

logger = configure_logging()


def handle_uploaded_music_file(f, title, Author, expansion):
    logger.info(f"Сохраняем музыку(Название: {title}, Автор: {Author})")
    with open(f"src/media/Music_Audios/{title}_{Author}.{expansion}", "wb+") as destination:

        for chunk in f.chunks():
            destination.write(chunk)


def handle_uploaded_image_file(f, title, Author, expansion):
    logger.info(f"Сохраняем изображение(Название: {title}, Автор: {Author})")
    with open(f"{BASE_DIR}/media/Music_Images/{title}_{Author}.{expansion}", "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def save_music_upload(request):
    logger.info(f"Получаем данные из формы для загрузки музыки")
    form = UploadMusic(request.POST, request.FILES)
    if form.is_valid():
        Title = form.data.get("Title")
        Author = form.data.get("Author")
        Image = request.FILES["Image"]
        Audio = request.FILES["Audio"]
        Image_name_expansion = Image.name.split(".")[1]
        Audio_name_expansion = Audio.name.split(".")[1]
        All_Authors = Authors.objects.all()
        try:
            Authors.objects.get(Name=Author)
            F = False
        except:
            F = True
        if F:
            Author_id = len(All_Authors) + 1
            New_Author = Authors(Name=Author)
            New_Author.save()
        else:
            Author_id = Authors.objects.get(Name=Author).id
        handle_uploaded_image_file(Image, Title, Author, Image_name_expansion)
        handle_uploaded_music_file(Audio, Title, Author, Audio_name_expansion)
        music = Music(
            Title=Title,
            Author=Author,
            Music=f"Music_Audios/{Title}_{Author}.{Audio_name_expansion}",
            Image=f"Music_Images/{Title}_{Author}.{Image_name_expansion}",
            Author_id=Author_id,
        )
        logger.info(f"Музыка успешно загружена на сайт")
        music.save()


def like_track(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        if request.GET.get("music_id") != None:
            logger.info(f"Пользователь лайкнул трек с id: {request.GET.get("music_id")}")
            Music_like_id: int = int(request.GET.get("music_id"))
            Favourite_track = Favourite_tracks.objects.filter(
                Track_id=Music_like_id, User_id=request.user.id
            )
            if len(Favourite_track) == 0:
                New_Favourite_track = Favourite_tracks(
                    Track_id=Music_like_id,
                    User_id=request.user.id,
                )
                New_Favourite_track.save()
            else:
                Favourite_track.delete()
