import requests
from django.utils.timezone import now
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import django
from django.conf import settings

# Настройка Django
if not settings.configured:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vacancy_parser.settings')
    django.setup()
from vacancy.models import Vacancies

from dotenv import load_dotenv

import time
import logging
# from exceptions import AbsentKeyError, FailingStatusError, StatusCodeError
from telebot import TeleBot, apihelper
load_dotenv()


logger = logging.getLogger(__name__)

stream_handler = logging.StreamHandler()
file_handler = logging.FileHandler('bot.log', 'w')

logger.addHandler(stream_handler)
logger.addHandler(file_handler)

PRACTICUM_TOKEN = os.getenv('PRACTICUM_TOKEN')
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')
BEARER = os.getenv('BEARER')
USER_AGENT = os.getenv('USER_AGENT')


def load_vacancies():
    params = {
        "text": "Python",
        "area": 1,
        "experience": "between1And3",
        "per_page": 50
    }
    headers = {
        "Authorization": BEARER,
        "HH-User-Agent": USER_AGENT
    }

    try:
        response = requests.get(
            "https://api.hh.ru/vacancies", params=params, headers=headers)
        data = response.json()

        for item in data['items']:
            if not Vacancies.objects.filter(id=item['id']).exists():
                Vacancies.objects.create(
                    title=item['name'],
                    # description=f"{item['snippet']['requirement'] or ''}\n{item['snippet']['responsibility'] or ''}",
                    # salary_from=item['salary']['from'],
                    # salary_to=item['salary']['to'],
                    # salary_currency=item['salary']['currency'],
                    # company=item['employer']['name'],
                    # allowed_time=now(),
                    # site='hh.ru',
                    site_id=item['id'],
                    # company_rating=0.0
                )
    except Exception as e:
        print(f"Error loading vacancies: {e}")


message_queryset = Vacancies.objects.all()
message = 'Список вакансий: \n'
for vacancy in message_queryset:
    message += f'{vacancy.title}\n'
if len(message) > 4096:
    message = message[:4090] + '...'
bot = TeleBot(TELEGRAM_TOKEN)


def send_message(bot, message):
    """Отправляет сообщение в Telegram чат."""
    try:
        bot.send_message(TELEGRAM_CHAT_ID, message)
        logger.debug(f'Бот отправил сообщение: {message}''')
        return True
    except apihelper.ApiException as telegram_error:
        logger.error(f'Ошибка отправки сообщения в Telegram: {telegram_error}')
        return False
    except requests.RequestException as connect_error:
        logger.error(f'Ошибка соединения: {connect_error}')
        return False


if __name__=='__main__':
    load_vacancies()
    time.sleep(10)
    send_message(bot, message)