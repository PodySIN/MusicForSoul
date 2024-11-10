"""
Модуль который отвечает за формы для музыки
"""

from django import forms


class UploadMusic(forms.Form):
    """
    Форма загрузки музыки на сайт
    """

    Title = forms.CharField(
        label="Название",
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Название",
                "class": "form-control",
            }
        ),
    )
    Author = forms.CharField(
        label="Автор",
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Автор",
                "class": "form-control",
            }
        ),
    )
    Image = forms.ImageField(
        label="Выберите изображение",
        required=True,
        widget=forms.ClearableFileInput(
            attrs={
                "class": "form-control",
            }
        ),
    )
    Audio = forms.FileField(
        label="Выберите аудио",
        required=True,
        widget=forms.ClearableFileInput(
            attrs={
                "class": "form-control",
            }
        ),
    )
