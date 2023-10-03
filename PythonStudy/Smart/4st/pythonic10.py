class DT:
    def __init__(self, attrs: dict):
        self.aaa = 200  # 1
        self.attrs = attrs

    @property  # 2
    def aab(self):
        return 300

    def __getattr__(self, attr):  # 3
        # print(attr)
        # return 100
        raise AttributeError("에러 내고 싶어요")


d = DT({})
print(d.aaa)
print(d.aab)
print(d.aac)

# 1. 진짜 그 변수가 있는지 찾아봄
# 2. property가 있는지 찾아봄
# 3. 매직 메서드 실행
