from django.db import models

from users.models import User


class Habit(models.Model):
    user = models.ForeignKey(
        User,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name="Пользователь",
        help_text="Укажите пользователя",
        related_name="habits",
    )
    place = models.CharField(
        max_length=250,
        blank=True,
        null=True,
        verbose_name="Место для выполнения привычки",
        help_text="Укажите место для выполнения привычки",
    )
    time = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name="Время",
        help_text="Укажите время, когда необходимо выполнить привычку",
    )
    action = models.CharField(
        max_length=300,
        blank=True,
        null=True,
        verbose_name="Действие",
        help_text="Укажите действие, которое представляет собой привычка",
    )
    is_pleasantly = models.BooleanField(
        blank=True,
        null=True,
        verbose_name="Признак приятной привычки",
        help_text="Укажите признак приятной привычки",
    )
    associated_habit = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="Связанная привычка",
        help_text="Укажите привычку, которая связана с другой привычкой (только для полезных привычек)",
    )
    periodicity = models.PositiveSmallIntegerField(
        default=1,
        verbose_name="Периодичность",
        help_text="Укажите периодичность выполнения привычки для напоминания в днях",
    )
    reward = models.CharField(
        max_length=300,
        blank=True,
        null=True,
        verbose_name="Вознаграждение",
        help_text="Укажите чем пользователь должен себя вознаградить после выполнения",
    )
    is_public = models.BooleanField(
        default=False,
        verbose_name="Признак публичности",
        help_text="Укажите можно ли публиковать привычку в общий доступ, чтобы другие пользователи могли брать в пример чужие привычки.",
    )
