import json
from django.test import TestCase, Client
from django.urls import reverse, resolve
from poll.models import Question, Choice
from django.utils.timezone import now


class TestQuestionAPI(TestCase):
    def test_404(self):
        response = Client().get('/question/0/')
        self.assertEqual(response.status_code, 404, '找不到時, HTTP GET 的 response code 要為 404')

    def test_retrieve(self):
        question = Question.objects.create(question_text='text', pub_date=now())
        response = Client().get('/question/{}/'.format(question.pk))
        self.assertEqual(response.status_code, 200, '正常時, HTTP GET 的 response code 要為 200')
