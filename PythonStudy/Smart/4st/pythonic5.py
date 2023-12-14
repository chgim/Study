class Test:
    def __init__(self, value):
        self._test_value = value

    # 함수를 속성값으로 만들음. 많은 활용도. 맘대로 값을 바꿀 수 있음. 외부에서 값을 세팅하지 못하게 막을 수 있음. readonly
    @property  # 데코레이터
    def test_value(self):
        if self._test_value < 10:
            return 100
        return self._test_value

    # 값을 할당할 때 알아서 값과 함께 함수 호출
    # 프로퍼티의 Setter는 프로퍼티에 값을 할당할 때 호출되는 메서드입니다. @property 데코레이터로 정의한 프로퍼티에 대응하는 setter는 @프로퍼티이름.setter로 정의됩니다.
    # Setter를 사용하면 값을 설정할 때 추가적인 로직을 수행할 수 있습니다.
    @test_value.setter
    def test_value(self, value):
        if value > 100:
            raise ValueError("100보다 큰 수는 안됩니다.")
        self._test_value = value


t = Test(0)
# 프로퍼티 test_value를 호출합니다. _test_value가 10 미만이므로 100이 출력됩니다.
print(t.test_value)
# _test_value 속성에 직접 접근하여 값을 출력합니다. (일반적으로 외부에서는 _로 시작하는 변수나 메서드에 직접 접근하지 않는 것이 관례입니다.)
print(t._test_value)
# private 용도로 사용하겠다. 클래스 안에서만 사용. python에는 private가 없기 때문에 개발자 사이에 룰처럼 _를 사용

# t.test_value = ("1234")
# # AttributeError: property 'test_value' of 'Test' object has no setter


# 프로퍼티 test_value에 값을 할당합니다. 이 때 setter 메서드가 호출되어, 새로운 값인 1234가 전달됩니다.
t.test_value = 1234
print(t.test_value)
#  @test_value.setter 사용으로 값 변경 가능 세팅


# C:\Users\kch11\Documents\GitHub\Study\PythonStudy\Smart>C:/Users/kch11/AppData/Local/Programs/Python/Python311/python.exe c:/Users/kch11/Documents/GitHub/Study/PythonStudy/Smart/4st/pythonic5.py
# 100
# 0
# Traceback (most recent call last):
#   File "c:\Users\kch11\Documents\GitHub\Study\PythonStudy\Smart\4st\pythonic5.py", line 34, in <module>
#     t.test_value = 1234
#     ^^^^^^^^^^^^
#   File "c:\Users\kch11\Documents\GitHub\Study\PythonStudy\Smart\4st\pythonic5.py", line 18, in test_value
#     raise ValueError("100보다 큰 수는 안됩니다.")
# ValueError: 100보다 큰 수는 안됩니다.
