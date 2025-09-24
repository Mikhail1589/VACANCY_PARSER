from django.apps import AppConfig


class VacancyConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'vacancy'

    def ready(self):
        # Импортируем здесь, чтобы избежать circular imports
        from api.utils import load_vacancies
        load_vacancies()
