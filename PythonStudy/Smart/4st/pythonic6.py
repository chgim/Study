# mangling
class Test:  # __ 언더바 두개는 클래스끼리 구분
    def __init__(self, value):
        self.__test_value = value


class Test2(Test):  # 상속
    def __init__(self, value):
        self.__test_value = value


t = Test(0)
# print(t.__test_value)
# AttributeError: 'Test' object has no attribute '__test_value'. Did you mean:'_Test__test_value'?
print(t._Test__test_value)

t = Test2(10)
print(t._Test2__test_value)
