from django.db import models


# https://docs.djangoproject.com/en/3.1/intro/tutorial02/


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', auto_now_add=True)


class Choice(models.Model):
    question = models.ForeignKey('poll.Question', on_delete=models.CASCADE, related_name='choices')
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
