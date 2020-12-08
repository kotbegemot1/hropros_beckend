from django.db import models
from django.urls import reverse, reverse_lazy

import datetime

from django.utils import timezone

# Create your models here.

class Question(models.Model):
    question_text = models.CharField('Вопрос', max_length=250)
    pub_date = models.DateTimeField('Дата публикации', default=timezone.now())

    def __str__(self):
        return self.question_text
    
    # def get_absolute_url(self):
    #     return reverse('polls:detail', kwargs={'pk': self.pk})

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
    
    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField('Вариант ответа', max_length=200)
    votes = models.IntegerField('Количество голосов',default=0)

    def __str__(self):
        return self.choice_text

    class Meta:
        verbose_name = "Ответ"
        verbose_name_plural = "Ответы"