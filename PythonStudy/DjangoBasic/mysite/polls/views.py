from django.http import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render

from django.urls import reverse
from .models import Choice, Question

# Create your views here.

def index(request):
    latest_question_list = Question.objects.all().order_by('-pub_date')[:5]
    # 쿼리 실행 안되어있음.
    context={'latest_question_list':latest_question_list,}
    return render(request, "index.html",context)
    # 쿼리를 실행하고 문자열 조인.
    

def detail(request, question_id):
    try:
       question=Question.objects.get(pk=question_id)
    except Question.DoesNotExist:# 특정 예외에 대해 catch 하는것을 권장
        raise Http404("Question does not exist.")
    return render(request, "detail.html", {"question":question}) # 파이썬은 예외 발생 시 그대로 프로그램 꺼지기 때문에 예외처리

def results(request, question_id):
    question=get_object_or_404(Question, pk=question_id)
    return render(request, "results.html", {"question":question})

def vote(request, question_id):
    question=get_object_or_404(Question, pk=question_id)
    try:
        selected_choice=question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, "detail.html",{
            "question":question,
            "error_message":"선택을 안했어 임마",}
        )
    else:
        selected_choice.votes+=1
        selected_choice.save()
        return HttpResponseRedirect(f"/polls/{question_id}/results/")  