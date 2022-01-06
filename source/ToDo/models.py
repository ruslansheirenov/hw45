from django.db import models

# Create your models here.

class Task(models.Model):
    STATUS_CHOICES = [('new', 'Новая'), ('in_progress', 'В процессе'), ('done', 'Сделано')]
    title = models.CharField(max_length=200, null=False, blank=False, verbose_name='Название')
    status = models.CharField(max_length=11, choices=STATUS_CHOICES, default='new', verbose_name='Статус')
    description = models.CharField(max_length=200, null=False, blank=False, verbose_name='Описание')
    detailed_description = models.TextField(max_length=2000, null=True, blank=True, verbose_name='Детальное Описание')
    date_of_completion = models.DateField(null=True, blank=True, verbose_name='Дата выполнения')

    def __str__(self):
        return f"{self.pk}. {self.title}"