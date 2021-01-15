from django.test import TestCase
from django.utils import timezone
from polls.models import Question
import datetime


class QuestionMethodTests(TestCase):
    # 测试方法
    def testWasPublishedRecentlyWithFuture(self):
        # 获取当前时间以后30天后的日期
        time = timezone.now() + datetime.timedelta(days=30)
        # 指定一个question pubdate属性为设置的未来的time
        futureQuestion = Question(pubDate=time)

        # 测试调用对象方法返回值和预期False是否一致
        self.assertIs(futureQuestion.wasPublishedRecently(), False)