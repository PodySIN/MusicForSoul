"""
Модуль который отвечает за модели для музыки
"""

from django.db import models


class Authors(models.Model):
    """
    Модель авторов музыки
    Name - имя автора
    """

    Name = models.CharField(default="", max_length=128)

    class Meta:
        db_table = "Authors"


class Music(models.Model):
    """
    Модель музыки
    Title - имя музыки
    Image - изображение музыки
    Music - музыка
    Author - автор
    Author_id - id автора
    """

    Title = models.CharField(default="", max_length=128)
    Image = models.CharField(default="", max_length=128)
    Music = models.CharField(default="", max_length=128)
    Author = models.CharField(default="", max_length=128)
    Author_id = models.IntegerField(default=1)

    class Meta:
        db_table = "Music"


class Favourite_tracks(models.Model):
    """
    Модель любимых треков пользователя
    Track_id - id трека
    User_id - id пользователя
    """

    Track_id = models.IntegerField(default=1)
    User_id = models.IntegerField(default=1)

    class Meta:
        db_table = "Favourite_tracks"
