from django.http import HttpResponse
from django.shortcuts import render

from .models import Question

# Create your views here.

def index(request):
    latest_question_list = Question.objects.all().order_by('-pub_date')[:5]
    # 쿼리 실행 안되어있음.
    output = ", ".join([q.question_text for q in latest_question_list])
    # 쿼리를 실행하고 문자열 조인.
    return HttpResponse(output)

def detail(request, question_id):
    return HttpResponse(f"You're looking at question {question_id}")

def results(request, question_id):
    return HttpResponse(f"You're looking at results of question {question_id}")

def vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}")