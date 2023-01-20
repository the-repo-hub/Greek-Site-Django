from django.db import models
from django.shortcuts import reverse
# Create your models here.

upload_to = 'forum/images'
class Theme(models.Model):
    head = models.CharField(max_length=150)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(blank=True, upload_to=upload_to)

    def __str__(self):
        return self.head

    def get_absolute_url(self):
        return reverse('theme', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'

class Post(models.Model):
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE, blank=True)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(blank=True, upload_to=upload_to)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

