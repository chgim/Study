# 데코레이터


# 어떤 함수를 실행할 때 로그인 후 동작하게 하고 싶음.
# login 여부를 확인 후 필터링 가능
# 근데 그러한 함수가 여러개일 경우를 가정
# login 여부를 확인하는 코드가 변동될 수 있음
# 이때 해당 코드를 여러개의 함수에서 다 바꾸기엔 비효율
# 그래서 데코레이터 함수를 제작
def original():  # 함수도 객체이다.
    print("original")


def login_required(func):
    if "is Login?":
        return func()
    print("You should log in")


original = login_required(original)


# a = original
# a()
