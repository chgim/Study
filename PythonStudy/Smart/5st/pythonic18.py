# 데코레이터
from functools import wraps  # 데코레이터를 정의할 때 사용되며, 데코레이트된 함수의 메타데이터를 유지하기 위해 사용됩니다.


def decorator(original):  # aa 함수가 인자로 적용됨 aa->original
    # Decorator factory to apply update_wrapper() to a wrapper function
    @wraps(original)  # 데코레이트된 함수의 메타데이터(예: __name__)를 원래 함수로부터 유지시킵니다.
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
print("---" * 10)
print(aa.__name__)  # decorated_function


# C:\Users\kch11\Documents\GitHub\Study\PythonStudy\Smart>C:/Users/kch11/AppData/Local/Programs/Python/Python311/python.exe c:/Users/kch11/Documents/GitHub/Study/PythonStudy/Smart/5st/pythonic18.py
# Decorated!
# 100
# After
# ------------------------------
# aa
