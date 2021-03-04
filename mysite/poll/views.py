import json
from django.http import HttpResponse, QueryDict
from django.utils.timezone import now
from django.views import View
from .models import Question, Choice


class QuestionAPIView(View):
    def post(self, request):
        text = json.loads(request.body).get('question_text')
        if len(text) > 200:
            return HttpResponse(status=400)
        Question.objects.create(question_text=text, pub_date=now())
        return HttpResponse()

    def put(self, request, pk):
        text = json.loads(request.body).get('question_text')
        question = Question.objects.get(pk=pk)
        if len(text) > 200:
            return HttpResponse(status=400)
        question.question_text = text
        question.save()
        return HttpResponse()
    elif request.method == 'DELETE':
        question = Question.objects.get(pk=pk)
        question.delete()
        return HttpResponse()

    def get(self, request, pk):
        try:
            question = Question.objects.get(pk=pk)
        except Question.DoesNotExist:
            return HttpResponse(status=404)

        data = dict(
            id=question.id,
            question_text=question.question_text,
            choices=list(
                dict(
                    id=choice.id,
                    choice_text=choice.choice_text,
                )
                for choice in Choice.objects.all()
            ),
        )
        return HttpResponse(json.dumps(data))
