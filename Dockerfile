# Указываем базовый образ
FROM python:3.11-slim

# Контактные сведения создателя образа
LABEL maintainer olegtimer@yandex.ru

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

RUN apt-get update \
    && apt-get install -y gcc libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Копируем файл с зависимостями и устанавливаем их
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Копируем остальные файлы проекта в контейнер
COPY . .

# Открываем порт 8000 для взаимодействия с приложением
EXPOSE 8000
# Определяем команду для запуска приложения
# CMD ["sh", "-c", "python3 manage.py collectstatic --noinput && gunicorn config.wsgi:application --bind 0.0.0.0:8000" ]
