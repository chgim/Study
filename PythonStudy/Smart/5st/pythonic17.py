# 데코레이터


def original():  # 함수도 객체이다.
    print("original")


def login_required(func):
    if "is Login?":
        return func()
    print("You should log in")


original = login_required(original)


# a = original
# a()
