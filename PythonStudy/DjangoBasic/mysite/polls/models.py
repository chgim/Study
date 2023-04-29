# 테이블 정의
from django.db import models # django.db.models.Model 클래스 상속받아 정의

# Create your models here.

# PK를 클래스에 지정하지 않고도 장고는 PK에 대한 속성을 NOT NULL 및 Autoincreasement로, 이름은 id로 해서 자동으로 만듬
class Question(models.Model): # 테이블
    question_text = models.CharField(max_length=256) # CharField: 문자열 데이터 저장하는 필드
    pub_date = models.DateTimeField(verbose_name="date published") # DateTimeField() 클래스에 정의한 date published -> pub_date에 대한 레이블 문구

    def __str__(self):
        return self.question_text

class Choice(models.Model): # 테이블
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # 필드를 외래키로 설정. Question 테이블과 일대다 관계 형성
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0) # InterField: 정수 데이터를 저장하는 필드

    def __str__(self):
        return self.choice_text


# 장고에서는 테이블을 하나의 클래스로 정의하고 테이블의 컬럼은 클래스의 변수(속성)으로 매핑

 