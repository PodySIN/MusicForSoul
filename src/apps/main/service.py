"""
Модуль для обработки данных и бд и получния базовых данных
"""

from apps.music_catalog.models import Music
from logger import configure_logging

logger = configure_logging()


def get_base_context(title, pagename):
    """
    Получения базовых данных
    :param title: имя сайта
    :param pagename: имя плашки сайта
    """
    logger.info(f"Получаем базовые данные")
    context = {
        "Title": title,
        "Pagename": pagename,
        "Absolute_Len": len(get_all_objects(Music)),
    }
    return context


def get_objects_form_db_by_id(Model, **kwargs):
    """
    Получение объекта из бд по ключи(по id и т.д)
    :param Model: модель, из которой нужно получить объект по ключам
    :param kwargs: ключи
    """
    logger.info(f"Получаем объекты по ключам")
    return Model.objects.get(**kwargs)


def get_filtred_objects(Model, **kwargs):
    """
    Фильтр объектов из бд по ключам
    :param Model: модель, из которой нужно получить объект по ключам
    :param kwargs: ключи
    """
    logger.info(f"Фильтруем объекты по ключам")
    return Model.objects.filter(**kwargs)


def get_all_objects(Model):
    """
    Получаем все объекты из бд
    :param Model: модель, из которой нужно получить все объекты
    """
    logger.info(f"Получаем все объекты из модели")
    return Model.objects.all()
