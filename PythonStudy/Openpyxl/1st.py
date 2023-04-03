class Test:
    a = 10

    def __init__(self):
        self.instance_variable = 100

    def func(self):
        print(self.instance_variable)
        print("Hello")

    @staticmethod 
    def func2():
        print("Hi")

    @classmethod
    def func3(cls):
        print(cls.a)

t = Test()
t.func()

Test.func2()
Test.func3()