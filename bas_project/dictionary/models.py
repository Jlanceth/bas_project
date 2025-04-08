from django.db import models

class DroneTerm(models.Model):
    term = models.CharField("Термин", max_length=100)
    translation = models.CharField("Перевод", max_length=100)
    definition = models.TextField("Определение") 

    def __str__(self):
        return self.term
