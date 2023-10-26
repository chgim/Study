# mixin
# 다중 상속 지원
# drf 페이지-> 장고는 mixin을 이용하여 api를 쉽게 만들 수 있음
# class는 상태값을 가질 수 있다.


class LoggerMixin:  # 상속 전용
    def log(self):
        print(self.data)


class A(LoggerMixin):
    def __init__(self, data):
        self.data = data


a = A("hello")
a.log()


# C:\Users\kch11\Documents\GitHub\Study\PythonStudy\Smart>C:/Users/kch11/AppData/Local/Programs/Python/Python311/python.exe c:/Users/kch11/Documents/GitHub/Study/PythonStudy/Smart/5st/pythonic13.py
# hello
