from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.http import Http404
from django.urls import reverse
from azure.storage.queue import QueueService

import datetime
import base64

from .models import Question

# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list
    }
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    queue_service = QueueService(account_name='firstsep9ed1', account_key='W+XOdAGrNzjtqTjCopNYZ5wX09Rfy1MTNLGwGnza6eofPkVqXMePyC5ovA+rkd3m4nDxEJeYcY0wCEcodLxyWQ==')
    #queue_service.create_queue('taskqueue')
    #message = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    message = base64.b64encode(bytes(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 'utf-8'))
    queue_service.put_message('test-python-queue', message.decode('ascii'))

    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))