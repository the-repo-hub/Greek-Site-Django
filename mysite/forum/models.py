from django.db import models
from django.shortcuts import reverse
# Create your models here.

class Post(models.Model):
    head = models.CharField(max_length=150)
    text = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    is_published = models.BooleanField()

    def __str__(self):
        return self.head

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
