import json
from django.http import HttpResponse, QueryDict
from django.utils.timezone import now
from .models import Question, Choice


def question(request, pk=None):
    if request.method == 'POST':
        text = json.loads(request.body).get('question_text')
        if len(text) > 200:
            return HttpResponse(status=400)
        Question.objects.create(question_text=text, pub_date=now())
        return HttpResponse()
    elif request.method == 'PUT':
        text = json.loads(request.body).get('question_text')
        if len(text) > 200:
            return HttpResponse(status=400)
        Question.objects.filter(pk=pk).update(question_text=text)
        return HttpResponse()
    elif request.method == 'DELETE':
        Question.objects.filter(pk=pk).delete()
        return HttpResponse()
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
