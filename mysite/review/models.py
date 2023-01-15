from django.db import models

# Create your models here.

class Phrases(models.Model):
    phrase = models.TextField()
    translation = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tense = models.ForeignKey('Tense', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.phrase

    class Meta:
        verbose_name = 'Фраза'
        verbose_name_plural = 'Фразы'


class Tense(models.Model):
    tense = models.CharField(max_length=150)

    class Meta:
        verbose_name = 'Время'
        verbose_name_plural = 'Времена'

    def __str__(self):
        return self.tense
