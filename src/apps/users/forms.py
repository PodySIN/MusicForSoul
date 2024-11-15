"""
Модуль, в котором прописаны все формы для пользователя
"""

from django import forms


class RegistrationForm(forms.Form):
    """
    Форма для регистрации пользователя в системе
    :param Username: Ник пользователя
    :param Password: Пароль пользователя
    :param RepeatPassword: Повтор пароля для пользователя
    """

    Username = forms.CharField(
        label="Имя пользователя",
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Логин",
                "class": "form-control",
            }
        ),
    )
    Password = forms.CharField(
        label="Пароль",
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Пароль",
            }
        ),
    )
    RepeatPassword = forms.CharField(
        label="Повтор пароля",
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Повтор пароля",
            }
        ),
    )


class LoginForm(forms.Form):
    """
    Форма для входа пользователя в систему
    :param username: Ник пользователя
    :param password: Пароль пользователя
    """

    username = forms.CharField(
        max_length=64,
        required=True,
        label="Логин",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Логин",
            }
        ),
    )
    password = forms.CharField(
        max_length=64,
        required=True,
        label="Пароль",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Пароль",
            }
        ),
    )
