import logging
from django.db.models import Model, CharField, DateField, ForeignKey, CharField, IntegerField
from django.test import TestCase
from poll import models



class TestModel(TestCase):
    def test_models(self):
        '''測試 Question, Choice 有沒有被定義'''

        assert hasattr(models, 'Question'), '請在 poll/models.py 裡定義 class Question'
        assert hasattr(models, 'Choice'), '請在 poll/models.py 裡定義 class Choice'

        assert issubclass(models.Question, Model), 'class Question 沒有繼承 django.db.models.Model'
        assert issubclass(models.Choice, Model), 'class Choice 沒有繼承 django.db.models.Model'

    def test_question_model(self):
        '''
            測試 Question 欄位有沒有定義
            有的話檢查 field type 有沒有正確
        '''

        Question = models.Question

        assert hasattr(Question, 'question_text'), 'class Question 沒有定義 question_text 欄位'
        assert hasattr(Question, 'pub_date'), 'class Question 沒有定義 pub_date 欄位'

        logger = logging.getLogger(__name__)
        fields = dict((field.name, field) for field in Question._meta.fields)

        if not isinstance(fields.get('question_text', None), CharField):
            logger.error('Question.question_text 不是 CharField')

        if not isinstance(fields.get('pub_date', None), DateField):
            logger.error('Question.pub_date 不是 DateField')

    def test_choice_model(self):
        '''
            測試 Question 欄位有沒有定義
            有的話檢查 field type 有沒有正確
        '''

        Choice = models.Choice

        assert hasattr(Choice, 'question'), 'class Choice 沒有定義 question 欄位'
        assert hasattr(Choice, 'choice_text'), 'class Choice 沒有定義 choice_text 欄位'
        assert hasattr(Choice, 'votes'), 'class Choice 沒有定義 votes 欄位'

        logger = logging.getLogger(__name__)
        fields = dict((field.name, field) for field in Choice._meta.fields)

        if not isinstance(fields.get('question', None), ForeignKey):
            logger.error('Choice.question_text 不是 ForeignKey')

        elif not fields['question'].model != models.Question:
            logger.error('Choice.question 不是 Question 的 ForeignKey')

        if not isinstance(fields.get('choice_text', None), CharField):
            logger.error('Choice.question_text 不是 CharField')

        if not isinstance(fields.get('votes', None), IntegerField):
            logger.error('Choice.question_text 不是 IntegerFIeld')
