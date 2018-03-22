from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse


from .models import Question

# Create your views here.

# HTTP RESPONSE --> ADDS BASIC TEXT TO YOUR WEBSITE
def index(request):

    # IMPORTED questions_text FROM Question Class FROM Models AND ORDERED BY pub_date
    latest_questions = Question.objects.order_by('-pub_date')[:5]


    # LOAD AND RETURN DATA
    context = {'latest_questions': latest_questions}    # PASSES lastest_questions to index.html
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    # question = Question.objects.get(pk = question_id)
    question = get_object_or_404(Question, pk = question_id)
    return render(request, 'polls/detail.html', {'question': question}) # PASSES question to detail.html


def results(request, question_id):
    return HttpResponse("These are the results of the question: %s" % question_id)


def vote(request, question_id):
    return HttpResponse("Vote on question: %s" % question_id)
