"""
Модуль отвечающий за отображение страниц (users).
"""

from django.contrib.auth import (
    logout as django_logout,
)
from django.contrib.auth.decorators import login_required

from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from apps.main.service import (
    get_base_context,
)
from apps.users.service import user_registration, user_login
from apps.users.forms import RegistrationForm, LoginForm
from logger import configure_logging

logger = configure_logging()


def registration_page(request: WSGIRequest) -> HttpResponse:
    """
    Страница регистрации пользователя в систему.
    :param request: запрос к странице.
    :return: страницу регистрации пользователя.
    """
    logger.info("Вход на страницу регистрации.")
    context: dict = get_base_context("Title", "")
    context["RegistrationForm"]: dict = RegistrationForm()
    logger.info("Собрали данные из контекста.")
    if request.method == "POST":
        user_registration(request)
    logger.info("По запросу с методом GET рендерим страницу.")
    return render(request, "pages/registration.html", context)


def login(request: WSGIRequest) -> HttpResponse:
    """
    Страница входа пользователя в систему.
    :param request: запрос к странице.
    :return: страницу входа пользователя в систему.
    """
    logger.info("Переходим на страницу входа в систему.")
    context: dict = get_base_context("Title", "")
    context["LoginForm"]: dict = LoginForm()
    logger.info("Получаем данные из context.")
    if request.method == "POST":
        user_login(request)
    logger.info("По запросу с методом GET рендерим страниц.")
    return render(request, "pages/login.html", context)


def logout(request: WSGIRequest) -> HttpResponse:
    """
    Выход пользователя из системы.
    :param request: запрос к странице.
    :return: на главную страницу.
    """
    logger.warning(f"Пользователь с ником: {request.user.username} выходит из системы!")
    django_logout(request)
    messages.add_message(request, messages.INFO, "Вы успешно вышли из аккаунта")
    return redirect("/")


@login_required
def profile_page(request: WSGIRequest) -> HttpResponse:
    """
    Страница отображения профиля пользователя.
    :param request: запрос к странице.
    :return: страницу профиля пользователя.
    """
    logger.info("Переходим на страницу профиля.")
    context: dict = get_base_context("Title", "")
    context["User"] = request.user.username
    logger.info("Рендерим страницу профиля страницу каталога.")
    return render(request, "pages/profile.html", context)
