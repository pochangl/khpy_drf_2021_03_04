import json
from django.http import HttpResponse, QueryDict
from django.utils.timezone import now
from rest_framework.serializers import ModelSerializer
from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView, GenericAPIView
from .models import Question, Choice


class ChoiceSerializer(ModelSerializer):
    class Meta:
        model = Choice
        fields = ('id', 'choice_text', 'votes')


class QuestionSerializer(ModelSerializer):
    choices = ChoiceSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ('id', 'question_text', 'choices')


class QuestionAPIView(CreateAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView, GenericAPIView):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
