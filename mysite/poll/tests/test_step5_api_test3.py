import json
import urllib
from django.test import TestCase, Client
from django.urls import reverse, resolve
from poll.models import Question, Choice
from django.utils.timezone import now


class TestQuestionAPI(TestCase):
    def test_create(self):
        data = {'question_text': 'text2'}
        response = Client().post('/question/', data=data, content_type='application/json')
        try:
            question = Question.objects.get()
        except Question.DoesNotExist:
            raise AssertionError('api 無法新增 Question')

    def test_create_error(self):
        data = {'question_text': 'text2' * 1000}
        response = Client().post('/question/', data=data, content_type='application/json')

        assert Question.objects.count() == 0, 'Create 時, 字串長度超過 200 時, 不應該讓 Request 成功'
        assert response.status_code == 400, 'Create 時, 字串長度超過 200 要回傳 HTTP Response code 400 (Request Error)'

    def test_update(self):
        question = Question.objects.create(question_text='text', pub_date=now())

        data = urllib.parse.urlencode({'question_text': 'text2'})
        response = Client().put('/question/{}/'.format(question.pk), data=data, content_type='application/json')
        new_question = Question.objects.get(pk=question.pk)

        assert question.question_text == 'text'
        assert new_question.question_text == 'text2', 'api 無法更改 question 的資料'

    def test_update(self):
        question = Question.objects.create(question_text='text', pub_date=now())

        data = urllib.parse.urlencode({'question_text': 'text2' * 1000})
        response = Client().put('/question/{}/'.format(question.pk), data=data, content_type='application/json')
        new_question = Question.objects.get(pk=question.pk)

        assert question.question_text == 'text', '資料有錯, 所以 question_text 不應該改變'
        assert response.status_code == 400, 'Create 時, 字串長度超過 200 要回傳 HTTP Response code 400 (Request Error)'

    def test_delete(self):
        question = Question.objects.create(question_text='text', pub_date=now())
        assert Question.objects.exists()

        response = Client().delete('/question/{}/'.format(question.pk))
        assert not Question.objects.exists(), 'api 無法刪除 question 的資料'
