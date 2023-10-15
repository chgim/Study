from functools import wraps


def logging_decorator(func=None, filename=None):
    if func is None:  # @logging_decorator(filename="test2")

        def decorator(func2):
            @wraps(func2)
            def decorated(*args, **kwargs):
                print(filename)
                res = func2(*args, **kwargs)
                return res

            return decorated

        return decorator
    else:

        @wraps(func)
        def decorated(*args, **kwargs):
            print("logging without arguments")
            res = func(*args, **kwargs)
            return res

        return decorated


@logging_decorator
def test():
    print("hh")


@logging_decorator(filename="test2")
def test2():
    print("hh")


test()
print("---" * 10)
test2()
