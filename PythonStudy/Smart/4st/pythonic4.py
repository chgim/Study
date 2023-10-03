# 컴프리헨션 - 할당 표현식
# 리스트, 튜플, 집합, 딕셔너리 가능
import dis  # 코드 오류 찾을 때 사용하기 좋음


def logic1():
    t = []
    for i in range(10):
        t.append(i * 10)
    return t


def logic2():  # 성능 향상
    t = [i * 10 for i in range(10)]  # 반복해서 10 곱하고 리스트 만든다음 프린트 - 스크립트 언어의 특징
    return t


dis.dis(logic1)
print("-" * 30)
dis.dis(logic2)

t = [i * 10 for i in range(10)]
t = [i * 10 for i in range(10) if i % 2 == 1]
# print(t)
# print(t[0])   #10
t = (i * 10 for i in range(10) if i % 2 == 1)
# print(t[0])   # error
# print(next(t))  # generator 인덱싱 불가능 반복문 돌 수 있음
# print(next(t))
# print(next(t))
# print(next(t))
# for a in t:
#   print(a)
# t = {f"key-{i}": i for i in range(10)}
t = {"key" for i in range(10)}
print(t)

t = [1, 2, 3, 1, 2, 3, 1, 2, 3]
t = set(t)
print(t)
print(len(t))
