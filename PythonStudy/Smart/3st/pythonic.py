# 자체 시퀀스 생성
# 파이썬의 인덱싱과 슬라이싱은 __getitem__이라는 매직 메서드로 동작한다.
# __getitem__은 myobject[key]와 같은 형태를 사용할 때 사용되는 메서드이다.
# 특히 __getitem__과 __len__을 사용하여 시퀀스나 이터러블 객체를 만들지 않고 키를 통해 객체의 특정 요소를 가져올 수 있다.
class Items:
    # __init__: 클래스의 생성자 메서드로, 초기화를 수행합니다. 가변 인수를 받아들이고, 이를 _values 리스트에 저장합니다.
    def __init__(self, *values):
        self._values = list(values)

    # 해당 클래스의 인스턴스를 iterable하게 만듭니다. 만약 item이 문자열이면 "Hello"를 반환하고, 그렇지 않으면 _values 리스트의 해당 인덱스의 값을 반환
    def __getitem__(self, item):
        if type(item) == str:
            return "Hello"
        return self._values[item]

    # len() 함수를 사용하여 해당 클래스의 길이를 반환
    def __len__(self):
        return len(self._values)


# items = Items(1, 2, 3, 4, 5)
# Items 클래스에서 __getitem__ 메서드를 정의했기 때문에 객체 items는 iterable 객체가 됩니다. 따라서 루프를 통해 각 항목을 순회할 수 있습니다.
items = Items("a", "b", "c")


for item in items:
    print(item)
# __len__ 메서드를 정의했기 때문에 len() 함수를 사용하여 해당 클래스의 길이를 반환
print(len(items))
# __getitem__ 메서드에서 item이 문자열인 경우 "Hello"를 반환하도록 정의했으므로, 여기서는 "Hello"가 출력
print(items["StringValue"])

# for문은 IndexError가 나올때까지 인덱스 반복
