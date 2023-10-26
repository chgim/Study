# dataclass
from dataclasses import dataclass


@dataclass
class Customer:  # 생성자를 직접 생성
    id: int
    name: str
    tel: str

    # def __init__(self)
    #     print("Hello")
    # dataclass를 쓸 경우에는 생성자를 그대로 쓰지 않음
    def __post_init__(self):  #  생성자를 직접 생성하기 때문에 해당 메서드를 통해 생성자 만들음
        self._first_name = self.name[0]

    # 데이터 클래스를 사용하더라도 직접 생성자를 만들 수 있습니다. 이 경우 __post_init__ 메서드를 사용하여 생성자를 정의합니다. 이 메서드는 객체가 생성된 후 호출됩니다.

    def __str__(self):  # 가능한 이유-> 객체를 문자열로 표현하는 메서드를 정의합니다. 이 경우 객체의 id 값을 출력합니다.
        return f"Customer(id={self.id})"

    @property
    def firstname(self):
        return self._first_name


# c = Customer(1, "김찬호", "01022222222")
# c2 = Customer(id=2, name="김진야", tel="01033333333")
# print(c2.id)


# with open("test2.csv", "r", encoding="utf-8") as f:
#     users = [line.strip().split(",") for line in f.readlines()]
# print(users)

with open("test2.csv", "r", encoding="utf-8") as f:
    users = [
        Customer(*line.strip().split(",")) for line in f.readlines()
    ]  #  파일 "test2.csv"에서 각 줄을 읽어서 쉼표로 분리하고, 그 값을 이용해 Customer 클래스의 객체를 생성하고 이를 리스트에 추가합니다.

for user in users:
    print(user)

for user in users:
    print(str(user))

for user in users:
    print(user.id, user.name, user.firstname)
