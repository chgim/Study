import time
from functools import wraps


def traced_time(func):
    @wraps(func)
    def wrapped(*args, **kwargs):
        s = time.time()

        res = func(*args, **kwargs)
        print(time.time() - s)
        return res

    return wrapped


@traced_time  # 바로 아래 있는 객체를 첫번째 인자 값으로 해서 함수 호출, return 값으로 바꿔치기
def f1():
    time.sleep(2)
    print("완료")


f1()
