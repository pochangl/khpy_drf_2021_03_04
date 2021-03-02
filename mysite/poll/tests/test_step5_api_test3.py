import json
import urllib
from django.test import TestCase, Client
from django.urls import reverse, resolve
from poll.models import Question, Choice
from django.utils.timezone import now


class TestQuestionAPI(TestCase):
    def test_update(self):
        question = Question.objects.create(question_text='text', pub_date=now())

        data = urllib.parse.urlencode({'question_text': 'text2'})
        response = Client().put('/question/{}/'.format(question.pk), data=data)
        new_question = Question.objects.get(pk=question.pk)

        assert question.question_text == 'text'
        assert new_question.question_text == 'text2', 'api 無法更改 question 的資料'
