from django.db import models

class Task(models.Model):
    title = models.CharField('Название', max_length=50)
    lyrics = models.TextField('Текст')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Текст'
        verbose_name_plural = 'Тексты'

# Create your models here.
