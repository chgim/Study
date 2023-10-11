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


@traced_time
def f1():
    time.sleep(2)
    print("완료")


f1()
