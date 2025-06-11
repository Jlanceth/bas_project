from django.db import models


class DroneTerm(models.Model):
    term_eng = models.CharField("Термин", max_length=100)
    abbr_eng = models.CharField("Термин на английском", max_length=100)
    category = models.CharField("Категория", max_length=100)
    part_references = models.CharField("Часть речи", max_length=100)
    term_rus = models.CharField("Термин на русском",max_length=100)
    definition_rus = models.TextField("Определение на русском")
    definition_eng = models.TextField("Определение на английском")
    context_eng = models.TextField("Контекст на английском")
    context_rus = models.TextField("Контекст на русском")

    def __str__(self):
        return self.term_eng
