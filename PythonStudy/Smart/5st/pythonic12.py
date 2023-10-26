# 다중 상속
# 다중 상속 시 코드 가독성 떨어짐


class A:
    def aa(self):
        print("aa")


class B:
    def aa(self):
        print("bb- aa")

    def bb(self):
        print("bb")


class C(A, B):  # A가 우선, 그다음 B
    pass


class D(B, A):  # B가 우선, 그 다음 A
    pass


c = C()

c.aa()  # 클래스 A의 함수 aa를 상속 받았는지 클래스 B의 함수 aa를 상속 받았는지 알기 힘듬. 설계 잘못된 코드
c.bb()

print("---" * 10)

d = D()

d.aa()
d.bb()

print(D.mro())


# C:\Users\kch11\Documents\GitHub\Study\PythonStudy\Smart>C:/Users/kch11/AppData/Local/Programs/Python/Python311/python.exe c:/Users/kch11/Documents/GitHub/Study/PythonStudy/Smart/5st/pythonic12.py
# aa
# bb
# ------------------------------
# bb- aa
# bb
# [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>]
