from django.apps import AppConfig


class DictionaryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'dictionary'

    def ready(self):
        # Импортируем здесь, чтобы избежать circular imports
        from .models import Language
        # Создаем языки при запуске приложения
        Language.initialize_languages()
