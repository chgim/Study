class Items:
    def __init__(self, *values):
        self._values = list(values)

    def __getitem__(self, item):
        if type(item) == str:
            return "Hello"
        return self._values[item]

    def __len__(self):
        return len(self._values)


# items = Items(1, 2, 3, 4, 5)
items = Items("a", "b", "c")


for item in items:
    print(item)

print(len(items))

print(items["StringValue"])

# for문은 IndexError가 나올때까지 인덱스 반복
