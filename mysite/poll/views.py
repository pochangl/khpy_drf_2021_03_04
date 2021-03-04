import json
from django.http import HttpResponse, QueryDict
from django.utils.timezone import now
from .models import Question, Choice


def question(request, pk=None):
    pass
