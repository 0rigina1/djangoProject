from django.db import models
from django.utils import timezone
import datetime


class Question(models.Model):
    questionText = models.CharField(max_length=200)
    pubDate = models.DateTimeField('date published')

    # 是否在当前发布的问卷
    def wasPublishedRecently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pubDate <= now

    wasPublishedRecently.admin_order_field = 'pubDate'
    wasPublishedRecently.boolean = True
    wasPublishedRecently.short_description = '最近公开？'

    def __str__(self):
        return self.questionText


class Choice(models.Model):
    # 关联外键
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choiceText = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return ''