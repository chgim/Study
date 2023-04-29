# Admin 사이트에 반영
from django.contrib import admin

from .models import Question, Choice # models.py 모듈에서 정의한 Question, Choice 클래스를 임포트

# Register your models here.

admin.site.register(Choice) # admin.site.register() 함수를 사용하여 임포트한 클래스를 Admin 사이트에 등록
admin.site.register(Question)

# 중요한점: 테이블을 새로 만들 때는 models.py와 admin.py 파일을 함께 수정해야 한다.