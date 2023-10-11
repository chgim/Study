# 가변인자

# 언패킹
first, second = [1, 2]
print(first, second)
# 가변인자
# 함수 x 변수에 값을 할당할때 언패킹이 일어나면 리스트로 만들어짐.
first, *rest = [1, 2, 3, 4, 5]
print(first, rest)

first, *rest = (1, 2, 3, 4, 5)
print(first, rest)

first, *rest, last = [1, 2, 3, 4, 5]
print(first, rest, last)

print("---" * 10)

#################################


def function(first, *args):
    print(first, args)


function(1, 2, 3, 4, 5, 6, 7)

print("---" * 10)

#################################


def function2(abc, **kwargs):  # 키워드 가변인자 딕셔너리로 받아짐
    print(kwargs)


function2(abc=100, bbb=200)

print("---" * 10)

#################################

DEFAULT_TIMEOUT = 10


def function3(timeout=DEFAULT_TIMEOUT, **kwargs):
    print(timeout)


function3()

#################################
