import time
from functools import wraps


def traced_time(func):
    @wraps(func)
    def wrapped(*args, **kwargs):
        s = time.time()  # 현재 시간

        res = func(*args, **kwargs)  # 함수 돌림
        print(time.time() - s)  # 함수 돌리고 지난 시간 계산
        return res

    return wrapped


@traced_time  # 바로 아래 있는 객체를 첫번째 인자 값으로 해서 함수 호출, return 값으로 바꿔치기
def f1():
    time.sleep(2)
    print("완료")


f1()


# C:\Users\kch11\Documents\GitHub\Study\PythonStudy\Smart>C:/Users/kch11/AppData/Local/Programs/Python/Python311/python.exe c:/Users/kch11/Documents/GitHub/Study/PythonStudy/Smart/5st/pythonic19.py
# 완료
# 2.0003271102905273
