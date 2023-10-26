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
# 리스트 컴프리헨션을 사용하여 i가 0부터 9까지 반복될 때마다 "key"를 요소로 갖는 리스트를 생성합니다.
# 이 리스트를 집합(set)으로 만들어 t에 할당합니다.
# 결과적으로 t는 10번의 "key" 요소를 가지는 집합이 됩니다.
t = [1, 2, 3, 1, 2, 3, 1, 2, 3]
t = set(t)

print(t)
print(len(t))
# 리스트: [1, 2, 3]
# 집합: {1, 2, 3}


# C:\Users\kch11\Documents\GitHub\Study\PythonStudy\Smart>C:/Users/kch11/AppData/Local/Programs/Python/Python311/python.exe c:/Users/kch11/Documents/GitHub/Study/PythonStudy/Smart/4st/pythonic4.py
#   6           0 RESUME                   0

#   7           2 BUILD_LIST               0
#               4 STORE_FAST               0 (t)

#   8           6 LOAD_GLOBAL              1 (NULL + range)
#              18 LOAD_CONST               1 (10)
#              20 PRECALL                  1
#              24 CALL                     1
#              34 GET_ITER
#         >>   36 FOR_ITER                26 (to 90)
#              38 STORE_FAST               1 (i)

#   9          40 LOAD_FAST                0 (t)
#              42 LOAD_METHOD              1 (append)
#              64 LOAD_FAST                1 (i)
#              66 LOAD_CONST               1 (10)
#              68 BINARY_OP                5 (*)
#              72 PRECALL                  1
#              76 CALL                     1
#              86 POP_TOP
#              88 JUMP_BACKWARD           27 (to 36)

#  10     >>   90 LOAD_FAST                0 (t)
#              92 RETURN_VALUE
# ------------------------------
#  13           0 RESUME                   0

#  14           2 LOAD_CONST               1 (<code object <listcomp> at 0x00000254E631DE40, file "c:\Users\kch11\Documents\GitHub\Study\PythonStudy\Smart\4st\pythonic4.py", line 14>)
#               4 MAKE_FUNCTION            0
#               6 LOAD_GLOBAL              1 (NULL + range)
#              18 LOAD_CONST               2 (10)
#              20 PRECALL                  1
#              24 CALL                     1
#              34 GET_ITER
#              36 PRECALL                  0
#              40 CALL                     0
#              50 STORE_FAST               0 (t)

#  15          52 LOAD_FAST                0 (t)
#              54 RETURN_VALUE

# Disassembly of <code object <listcomp> at 0x00000254E631DE40, file "c:\Users\kch11\Documents\GitHub\Study\PythonStudy\Smart\4st\pythonic4.py", line 14>:
#  14           0 RESUME                   0
#               2 BUILD_LIST               0
#               4 LOAD_FAST                0 (.0)
#         >>    6 FOR_ITER                 7 (to 22)
#               8 STORE_FAST               1 (i)
#              10 LOAD_FAST                1 (i)
#              12 LOAD_CONST               0 (10)
#              14 BINARY_OP                5 (*)
#              18 LIST_APPEND              2
#              20 JUMP_BACKWARD            8 (to 6)
#         >>   22 RETURN_VALUE
# {'key'}
# {1, 2, 3}
# 3
