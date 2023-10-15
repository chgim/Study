import datetime
from functools import wraps


def logging_decorator(func):
    @wraps(func)
    def decorated(*args, **kwargs):  # 인자값이 얼마나 있는지 모르니깐 가변인자 사용
        now = datetime.datetime.now()
        fnt = now.strftime("%Y-%m-%d %H:%M:%S")
        name = func.__name__

        print(f"[{fnt}] Called [{name}{args},{kwargs}]")

        res = func(*args, **kwargs)
        return res

    return decorated


def logging_decorator2(func=None, filename=None):
    if func is None:

        def decorated(func):
            @wraps(func)
            def decorated(*args, **kwargs):  # 인자값이 얼마나 있는지 모르니깐 가변인자 사용
                now = datetime.datetime.now()
                fnt = now.strftime("%Y-%m-%d %H:%M:%S")
                name = func.__name__
                with open(filename, "a", encoding="utf-8") as f:
                    f.write(f"[{fnt}] Called [{name}{args},{kwargs}]\n")

                res = func(*args, **kwargs)
                return res

            return decorated

        return decorated
    else:

        @wraps(func)
        def decorated(*args, **kwargs):  # 인자값이 얼마나 있는지 모르니깐 가변인자 사용
            now = datetime.datetime.now()
            fnt = now.strftime("%Y-%m-%d %H:%M:%S")
            name = func.__name__

            print(f"[{fnt}] Called [{name}{args},{kwargs}]")

            res = func(*args, **kwargs)
            return res

        return decorated
