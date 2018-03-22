from django.shortcuts import render

from django.http import HttpResponse
from .models import Question

# Create your views here.

# HTTP RESPONSE --> ADDS BASIC TEXT TO YOUR WEBSITE
def index(request):

    # IMPORTED pub_date FROM Question Class FROM Models
    # GET QUESTION OBJECTS AND ORDER THEM BY DATE
    # JOIN THEM OUT OUTPUT AND RETURN IT IN HTTP REQUEST
    lastest_questions = Question.objects.order_by('-pub_date')[:5]
    output = ", ".join(q.question_text for q in lastest_questions)
    return HttpResponse(output)


def detail(request, question_id):
    return HttpResponse("This is the detail view of the question: %s" % question_id)


def results(request, question_id):
    return HttpResponse("These are the results of the question: %s" % question_id)


def vote(request, question_id):
    return HttpResponse("Vote on question: %s" % question_id)
