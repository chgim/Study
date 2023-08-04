from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from member.models import Member

from .models import Question
# Create your views here.


def index(request):
    latest_question_list = Question.objects.all().order_by('-pub_date')[:5]
    # 쿼리 실행 안되어있음.
    output = ", ".join([q.question_text for q in latest_question_list])
    # 쿼리를 실행하고 문자열 조인.
    return HttpResponse(output)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "detail.html", {"question": question})


def cookie(request, quesiton_id):
    context = {}
    member_id = request.session.get("member_id")
    if member_id:
        member = Member.objects.get(px=member_id)
        context['member'] = member

    context['question'] = Question.objects.get(pk=quesiton_id)
    return render(request, "signup.html", context)


def results(request, question_id):
    return HttpResponse(f"You're looking at results of question {question_id}")


def vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}")
