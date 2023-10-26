from functools import wraps


def logging_decorator(data):
    def decorator(func):
        @wraps(func)
        def decorated(*args, **kwargs):  # 인자값이 얼마나 있는지 모르니깐 가변인자 사용
            print(data)
            res = func(*args, **kwargs)
            return res

        return decorated

    return decorator


# @logging_decorator  # @가 함수 호출시킴. 함수를 한번 더 감싸줬기 때문에 작동불가
# def test():
#     print("hh")


# logging_decorator("test2") 만으로 함수 호출 됨, test2가 인자로 들어가버림.@에 전달한 값은 함수의 리턴값(호출 했으니깐). 결국 해당 함수 호출의 결과값을 호출함. 함수 호출을 직접 하기 때문에 데코레이터를 반환하는 함수를 만들어줘야함
# logging_decorator("test2") 함수의 결과값이 decorator. @decorator 상태로 또 작동
@logging_decorator("test2")
def test2():
    print("hh")


test2()
