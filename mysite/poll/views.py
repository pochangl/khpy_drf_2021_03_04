import json
from django.http import HttpResponse
from .models import Question, Choice


def question(request, id):
    try:
        question = Question.objects.get(id=id)
    except Question.DoesNotExist:
        return HttpResponse(status=404)

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
    try:
        choice = Choice.objects.get(id=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist) as err:
        return HttpResponse(status=401)
    choice.votes += 1
    choice.save()
    return HttpResponse(status=201)
