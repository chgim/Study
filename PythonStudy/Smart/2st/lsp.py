# 파이썬은 type이 강력한 언어는 아니지만 type를 쓰는것을 권장
# 오버라이딩 할 때 인터페이스, 리턴값 맞춰서 쓰기
# 아래의 예시는 부적합 
class Event: 
    def condition(self, data: str) -> bool:
        return False


class UnknownEvent(Event):
    def condition(self, data: list) -> bool:
        data.append(10)
        return True
    

a = UnknownEvent()
print(a.condition([1, 2, 3]))


a = Event()
print(a.condition("123"))


def test(arg: Event):
    print(arg.condition("aaaa"))


test(Event())
test(UnknownEvent())