"""
Модуль отвечающий за главную страницу
"""

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from apps.main.service import get_base_context
from logger import configure_logging

logger = configure_logging()


def index_page(request: HttpRequest) -> HttpResponse:
    """
    Показ главной страницы сайта
    """
    logger.info("Загружаем главную страницу")
    context = get_base_context("Title", "")
    return render(request, "pages/index.html", context)
