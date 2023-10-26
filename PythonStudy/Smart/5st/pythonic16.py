# 위치 전용 인자
a = "String"
print(a.startswith("S"))

print("---" * 10)


def func(__a, /):  # 슬래시를 이용하여 위치 전용 인자 만들기
    print(__a)


func(10)
# func(__a=100)
# TypeError: func() got some positional-only arguments passed as keyword arguments: 'a'


# 키워드 전용 인자

print("---" * 10)


def func2(x, y, *args, kw1):
    print(x, y)


func2(10, 20, 30, 40, 50, kw1=60)

# C:\Users\kch11\Documents\GitHub\Study\PythonStudy\Smart>C:/Users/kch11/AppData/Local/Programs/Python/Python311/python.exe c:/Users/kch11/Documents/GitHub/Study/PythonStudy/Smart/5st/pythonic16.py
# True
# ------------------------------
# 10
# ------------------------------
# 10 20
