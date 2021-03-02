import json
from django.test import TestCase, Client
from django.urls import reverse, resolve
from poll.models import Question, Choice
from django.utils.timezone import now


class TestQuestionAPI(TestCase):
    def test_url(self):
        assert resolve('/question/3/'), '問卷調查網址 /question/3/ 不存在'

    def test_retrieve(self):
        question = Question.objects.create(question_text='text', pub_date=now())

        response = Client().get('/question/{}/'.format(question.pk))

        data = json.loads(response.content)
        assert 'id' in data, 'Question API 沒有 id 的資訊'
        assert 'question_text' in data, 'Question API 沒有 question_text 的資訊'


class TestVoteAPI(TestCase):
    def test_vote(self):
        question = Question.objects.create(question_text='text', pub_date=now())
        choice = Choice.objects.create(question=question, choice_text='choice', votes=0)

        assert choice.votes == 0
        data = {'choice': choice.pk}
        response = Client().post(path='/vote/', data=data)
        assert response.status_code != 404, '投票網址 /vote/ 沒有定義'

        new_choice = Choice.objects.get(pk=choice.pk)

        assert new_choice.votes == 1, 'POST {} 到 /vote/ 後, 投票結果沒有 +1'.format(data)
