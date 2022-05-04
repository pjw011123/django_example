from django.shortcuts import render, get_object_or_404
from polls.models import Question, Choice
from django.html import HttpResponseRedirect
from django.urls import reverse

def index(request):...

def detail(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    print(1)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        return render(request, 'first_app/')
