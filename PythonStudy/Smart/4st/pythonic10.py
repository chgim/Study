class DT:
    def __init__(self, attrs: dict):
        self.aaa = 200  # 1
        self.attrs = attrs

    @property  # 2
    def aab(self):
        return 300

    # 3 객체에서 속성을 찾을 수 없을 때 호출됩니다. raise AttributeError("에러 내고 싶어요"): AttributeError를 발생시켜 에러를 일으킵니다.
    def __getattr__(self, attr):
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
