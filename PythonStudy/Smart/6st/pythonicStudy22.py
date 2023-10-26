from functools import wraps


def logging_decorator(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        res = func(*args, **kwargs)
        return res

    return decorated


@logging_decorator
def test():
    print("test")


test()
