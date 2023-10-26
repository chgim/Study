# 호출형 객체


class Size:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __call__(self):
        print(self.width * self.height)


s = Size(100, 200)  # 생성자 함수 호출, 객체 변수 생성
s()  # 객체 호출
print("---" * 20)
print(s.width)
print(s.height)  # 객체는 상태값을 가질 수 있음. 메서드도 여러개 만들 수 있음
print("---" * 20)


def size(width, height):  # 함수는 휘발성
    print(width * height)


size(100, 300)


# C:\Users\kch11\Documents\GitHub\Study\PythonStudy\Smart>C:/Users/kch11/AppData/Local/Programs/Python/Python311/python.exe c:/Users/kch11/Documents/GitHub/Study/PythonStudy/Smart/5st/pythonic11.py
# 20000
# ------------------------------------------------------------
# 100
# 200
# ------------------------------------------------------------
# 30000
