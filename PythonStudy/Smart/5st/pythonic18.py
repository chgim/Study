# 데코레이터
from functools import wraps


def decorator(original):  # aa 함수가 인자로 적용됨 aa->original
    # Decorator factory to apply update_wrapper() to a wrapper function
    @wraps(original)
    def decorated_function(*args, **kwargs):
        print("Decorated!")
        res = original(*args, **kwargs)
        print("After")
        return res

    return decorated_function


@decorator  # 바꿔치기
def aa(value):
    print(value)


aa(100)
print(aa.__name__)  # decorated_function
