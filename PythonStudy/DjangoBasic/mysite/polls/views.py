from django.http import Http404, HttpResponseRedirect # vote에서 redirect가 필요 임포트
from django.shortcuts import get_object_or_404, render

from django.urls import reverse # vote URL 처리를 위해 임포트
from .models import Choice, Question # Question, Choice 테이블에 액세스 하기 위해 임포트

# Create your views here.

def index(request): # request 객체는 뷰 함수의 필수 인자
    latest_question_list = Question.objects.all().order_by('-pub_date')[:5]
    # 템플릿에게 넘겨줄 객체의 이름은 latest_question_list. pub_date 컬럼의 역순으로 정렬하여 5개의 최근 Question 객체를 가져와서 만듬

    # 쿼리 실행 안되어있음.
    context={'latest_question_list':latest_question_list} # 템플릿에 파이썬 사전 타입으로 템플릿에 사용될 변수명, 변수명에 해당하는 객체를 매핑
    return render(request, "index.html",context) # render 함수는 템플릿 파일인 index.html에 centext 변수를 적용해서 HttpResponse 객체 반환(render) 
    # 쿼리를 실행하고 문자열 조인.
    

def detail(request, question_id): # request는 필수 인자. 추가적으로 question_id 인자를 더 받음.
    try:
       question=Question.objects.get(pk=question_id) # question 모델 클래스로부터 pk=question_id 검색조건에 맞는 객체 조회. 없으면 에러
    except Question.DoesNotExist:# 특정 예외에 대해 catch 하는것을 권장
        raise Http404("Question does not exist.")
    return render(request, "detail.html", {"question":question}) # 파이썬은 예외 발생 시 그대로 프로그램 꺼지기 때문에 예외처리

def results(request, question_id):
    question=get_object_or_404(Question, pk=question_id) # get_object_or_404: 오브젝트 가져오거나 404
    return render(request, "results.html", {"question":question})

def vote(request, question_id):
    question=get_object_or_404(Question, pk=question_id)
    try:
        selected_choice=question.choice_set.get(pk=request.POST['choice']) # 폼 데이터에서 키가 'choice'에 해당하는 값인 choice.id를 스트링으로 리턴
    except (KeyError, Choice.DoesNotExist): # 폼의 post 데이터에서 'choice' 키가 없다면 KeyError익셉션 발생, 검색조건에 맞는 객체 없으면 Choice.DoesNotExist익셉션 발생
        return render(request, "detail.html",{ # 익셉션 발생 시 render()함수에 의해 question과error_message 변수를 deatil.html 템플릿으로 전달.
            "question":question,
            "error_message":"선택을 안했어 임마",}
        )
    else:
        selected_choice.votes+=1 #choice객체.votes 속성, 즉 선택 카운트를 +1 증가
        selected_choice.save() # 변경사항을 choice 테이블에 저장
        return HttpResponseRedirect(f"/polls/{question_id}/results/") # vote 함수가 반환하는 객체는 HttpResponseRedirect. 리다이랙트할 타겟 URL을 담은 HttpResponseRedirect 객체를 반환 