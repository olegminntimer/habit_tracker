from datetime import timedelta

import requests
from celery import shared_task
from django.utils import timezone

from config import settings
from habit.models import Habit


@shared_task
def send_telegram_message():
    """Отправляет уведомления в Телеграм о предстоящих привычках"""
    habits = Habit.objects.all()
    for habit in habits:
        time_difference = abs(timezone.now() - habit.time)
        if time_difference < timedelta(seconds=3600):
            text = f"В {habit.time.strftime('%H:%M %d.%m.%Y')} наступает" f" время для {habit.action} в {habit.place}!"
            params = {
                "text": text,
                "chat_id": habit.user.tg_chat_id,
            }
            requests.get(f"{settings.TELEGRAM_URL}{settings.TELEGRAM_TOKEN}/sendMessage", params=params)
            habit.time += timedelta(days=habit.periodicity)
            habit.save()
