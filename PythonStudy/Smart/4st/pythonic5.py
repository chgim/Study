class Test:
    def __init__(self, value):
        self._test_value = value

    # 함수를 속성값으로 만들음. 많은 활용도. 맘대로 값을 바꿀 수 있음. 외부에서 값을 세팅하지 못하게 막을 수 있음. readonly
    @property
    def test_value(self):
        if self._test_value < 10:
            return 100
        return self._test_value

    # 값을 할당할 떄 알아서 값과 함께 함수 호출
    @test_value.setter
    def test_value(self, value):
        if value > 100:
            raise ValueError("100보다 큰 수는 안됩니다.")
        self._test_value = value


t = Test(0)
print(t.test_value)
print(t._test_value)
# private 용도로 사용하겠다. 클래스 안에서만 사용. python에는 private가 없기 때문에 개발자 사이에 룰처럼 _를 사용

# t.test_value = ("1234")
# # AttributeError: property 'test_value' of 'Test' object has no setter

t.test_value = 1234
print(t.test_value)
#  @test_value.setter 사용으로 값 변경 가능 세팅
