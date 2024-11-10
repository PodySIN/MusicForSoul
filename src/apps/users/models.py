from django.contrib.auth.models import AbstractUser


class Users(AbstractUser):
    """
    Модель пользователя
    """

    class Meta:
        db_table = "Users"
