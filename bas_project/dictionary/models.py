from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


LANGUAGES = [
    {'code': 'ru', 'name': 'Русский'},
    {'code': 'en', 'name': 'Английский'},
    {'code': 'fr', 'name': 'Французский'},
    {'code': 'es', 'name': 'Испанский'},
    {'code': 'cn', 'name': 'Китайский'},
]


class Language(models.Model):
    code = models.CharField(max_length=5, unique=True)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    @classmethod
    def initialize_languages(cls):
        """Создает языки из константы LANGUAGES если их нет"""
        for lang in LANGUAGES:
            cls.objects.get_or_create(
                code=lang['code'],
                defaults={'name': lang['name']}
            )


class DroneTerm(models.Model):
    term_eng = models.CharField("Термин", max_length=100)
    abbr_eng = models.CharField("Термин на английском", max_length=100)
    category = models.CharField("Категория", max_length=100)
    part_references = models.CharField("Часть речи", max_length=100)
    term_rus = models.CharField("Термин на русском",max_length=100)
    abbr_rus = models.CharField("Аббревиатура на русском", max_length=100, blank=True, default='')
    definition_rus = models.TextField("Определение на русском")
    definition_eng = models.TextField("Определение на английском")
    context_eng = models.TextField("Контекст на английском")
    context_rus = models.TextField("Контекст на русском")
    language = models.ForeignKey(
        Language,
        on_delete=models.CASCADE,
        default=1
    )

    def __str__(self):
        return self.term_eng


class SearchHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    term = models.ForeignKey(DroneTerm, on_delete=models.CASCADE)
    query = models.CharField(max_length=100)
    searched_at = models.DateTimeField(auto_now_add=True)


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    term = models.ForeignKey('DroneTerm', on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'term')
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранные'

    def __str__(self):
        return f'{self.user.username} → {self.term.term_eng}'