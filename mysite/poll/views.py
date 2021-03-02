import json
from django.http import HttpResponse
from .models import Question, Choice


def question(request, id):
    question = Question.objects.get(id=id)
    data = dict(
        id=question.id,
        question_text=question.question_text,
        choices=list(
            dict(
                id=question.id,
                choice_text=question.choice_text,
            )
            for question in question.choices.all()
        ),
    )
    return HttpResponse(json.dumps(data))


def vote(request):
    choice = Choice.objects.get(id=request.POST.get('choice'))
    choice.votes += 1
    choice.save()
    return HttpResponse()
