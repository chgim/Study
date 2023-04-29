
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:question_id>/", views.detail, name="detail"), # "<int:question_id>/ : URL,  views.detail, name="detail": 처리함수(뷰)
    # <int:question_id> 위와같이 꺾쇠 사용 이유: URL 패턴의 일부 문자열 추출. ex)int:question_id 와 같이 <>(Path Converter) 부분이 해당 문자열일 때만 매핑.
    # 매치된 경우 매치된 문자열을 인자명 question_id에 할당. 요청 URL이  "<int:question_id>/" 이면 뷰 함수를 views.result(request, question_id=4)처럼 호출
    path("<int:question_id>/results/", views.results, name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
    # 매치된 URL은 뷰를 호출. 호출 시 HttpRequest 객체와 매칭할 때 추출된 단어들을 뷰에 인자로 넘겨줌. 
]
    # URL과 처리함수를 별도로 정의하고 이 둘을 매핑하는 방법: 유연성
    # URL과 뷰는 1:1 관계(N:1도 가능)로 매핑 URL/뷰 매핑: URLconf라고 하며 urls.py 파일에 작성
    # URL 모듈을 계층적으로 구성하면 변경도 쉽고 확장이 용이함