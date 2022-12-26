# Python 개념 정리

## 자료형 종류

숫자형, 리스트 자료형, 튜플 자료형, 딕셔너리 자료형, 집합 자료형, 불 자료형

## 주석

한줄 주석: #
여러줄 주석: """ ~ """, ''' ~ '''

## 문자열

### 문자열 포매팅

문자열 안에 어떤 값을 삽입하는 방법

```python run
m1="I eat %d apples." % 3
print(m1) # 'I eat 3 apples.'
m2="I eat %s apples." % "five"
print(m2) # 'I eat five apples.'
```

#### 2개 이상의 값 넣기

```python run
number = 10
day = "three"
ans="I ate %d apples. so I was sick for %s days." % (number, day)
print(ans) # 'I ate 10 apples. so I was sick for three days.'
```

#### format 함수를 사용한 포매팅

```python run
q1="I eat {} apples".format(3)
print(q1) # 'I eat 3 apples'
q2="My name is {}".format("조희진")
print(q2)
```

#### 문자열 슬라이싱

a[시작 번호:끝 번호] -> 끝 번호는 포함 X

```python run
a = "Life is too short, You need Python"
print(a[0:4]) # 'Life'
```

## 리스트와 투플의 차이점

- 리스트는 [ ]으로 둘러싸지만 튜플은 ( )으로 둘러싼다.
- 리스트는 요소 값의 생성, 삭제, 수정이 가능하지만 튜플은 요소 값을 바꿀 수 없다.

## for문

```python run
for 변수 in 리스트(또는 튜플, 문자열):
    수행할 문장1
    수행할 문장2
    ...
```

```python run
test_list = ['one', 'two', 'three']
for i in test_list:
    print(i) ## ...one...two...three
```

### for문의 활용

```python run
a = [(1,2), (3,4), (5,6)]
for (first, last) in a:
    print(first + last) ## ...3...7...11
```

```python run
marks = [90, 25, 67, 45, 80]

number = 0
for mark in marks:
    number = number +1
    if mark >= 60:
        print("%d번 학생은 합격입니다." % number)
    else:
        print("%d번 학생은 불합격입니다." % number)
```

### range 함수

```python run
add = 0
for i in range(1, 11):
    add = add + i
print(add) # 55
```

range(1, 11)은 숫자 1부터 10까지(1 이상 11 미만)의 숫자를 데이터로 갖는 객체이다.

### for와 range를 이용한 구구단

```python run
for i in range(2,10):        # 1번 for문
    for j in range(1, 10):   # 2번 for문
        print(i*j, end=" ")
    print('')
...
2 4 6 8 10 12 14 16 18
3 6 9 12 15 18 21 24 27
4 8 12 16 20 24 28 32 36
5 10 15 20 25 30 35 40 45
6 12 18 24 30 36 42 48 54
7 14 21 28 35 42 49 56 63
8 16 24 32 40 48 56 64 72
9 18 27 36 45 54 63 72 81
```

### 리스트 컴프리헨선

리스트 안에 for문을 포함하는 리스트 컴프리헨션을 사용하면 좀 더 편리하고 직관적인 프로그램을 만들 수 있다.

```python
[표현식 for 항목 in 반복가능객체 if 조건문]
```

```python
a = [1,2,3,4]
result = []
for num in a:
    result.append(num*3)

print(result) # [3, 6, 9, 12]
```

기존 코드

```python
a = [1,2,3,4]
result = [num * 3 for num in a]
print(result) # [3, 6, 9, 12]
```

리스트 컴프리헨션

```python
a = [1,2,3,4]
result = [num * 3 for num in a if num % 2 == 0]
print(result) # [6, 12]

```

[1,2,3,4] 중에서 짝수에만 3을 곱하고 싶은 경우

## if문 구조

```python run
if 조건문:
    수행할 문장1
    수행할 문장2
    ...
else:
    수행할 문장A
    수행할 문장B
    ...
```

```python run
money = True
if money:
    print("택시를 타고 가라")
else:
    print("걸어 가라")
```

기본 구조

### elif 구조

```python run
If <조건문>:
    <수행할 문장1>
    <수행할 문장2>
    ...
elif <조건문>:
    <수행할 문장1>
    <수행할 문장2>
    ...
elif <조건문>:
    <수행할 문장1>
    <수행할 문장2>
    ...
...
else:
   <수행할 문장1>
   <수행할 문장2>
   ...
```

기본 구조

```python run
pocket = ['paper', 'cellphone']
card = True
if 'money' in pocket:
    print("택시를 타고가라")
elif card:
    print("택시를 타고가라")
else:
    print("걸어가라")
```

## while문 구조

```python run
while <조건문>:
    <수행할 문장1>
    <수행할 문장2>
    <수행할 문장3>
    ...
```

```python run
treeHit = 0
while treeHit < 10:
    treeHit = treeHit +1
    print("나무를 %d번 찍었습니다." % treeHit)
    if treeHit == 10:
        print("나무 넘어갑니다.")
```

```python run
coffee = 10
while True:
    money = int(input("돈을 넣어 주세요: "))
    if money == 300:
        print("커피를 줍니다.")
        coffee = coffee -1
    elif money > 300:
        print("거스름돈 %d를 주고 커피를 줍니다." % (money -300))
        coffee = coffee -1
    else:
        print("돈을 다시 돌려주고 커피를 주지 않습니다.")
        print("남은 커피의 양은 %d개 입니다." % coffee)
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지 합니다.")
        break
```

    break를 통해 while문을 강제로 빠져나올 수 있다.

```python run
a = 0
while a < 10:
    a = a + 1
    if a % 2 == 0: continue
    print(a)
```

continue문을 통해 while문을 빠져나가지 않고 while문의 맨 처음(조건문)으로 다시 돌아가게 만들 수 있다.

## 함수 구조

```python run
def 함수명(매개변수):
    <수행할 문장1>
    <수행할 문장2>
    ...
```

기본 구조

```python run
def add(a, b): # a,b는 매개변수(함수에 전달된 값을 저장하는 변수)
    return a + b

a=3
b-4
c=add(a,b) # 인수(함수에 전달하는 값)
print(c) # 7

```

### 여러개의 입력값을 받는 함수

```python run
def add_many(*args):
    result = 0
    for i in args:
        result = result + i
    return result

print(add_many(1,2,3,4,5,6,7,8,9,10)) # 55
```

*args처럼 매개변수 이름 앞에 *을 붙이면 입력값을 전부 모아서 튜플로 만들어 준다.

## 클래스 구조

```python run
class FourCal: # 클래스
    def __init__(self, first, second): # 생성자
        self.first = first
        self.second = second
    def add(self): # 메서드
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result
```

### 클래스 상속

```python run
    class MoreFourCal(FourCal):
        def pow(self):
            result = self.first ** self.second
            return result
```

클래스를 상속하기 위해서는 다음처럼 클래스 이름 뒤 괄호안에 상속할 클래스 이름을 넣어주면 된다.

### 메서드 오버라이딩

```python run
class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0:  # 나누는 값이 0인 경우 0을 리턴하도록 수정
            return 0
        else:
            return self.first / self.second
```

부모 클래스에 있는 메서드를 동일한 이름으로 다시 만드는 것을 메서드 오버라이딩이라고 한다.
메서드를 오버라이딩하면 부모클래스의 메서드 대신 오버라이딩한 메서드가 호출된다.

## 모듈

파이썬에서 모듈은 하나의 .py 파일이다.
모듈이란 함수나 변수 또는 클래스를 모아 놓은 파이썬 파일이다.
모듈은 다른 파이썬 프로그램에서 불러와 사용할 수 있게끔 만든 파이썬 파일이라고도 할 수 있다.

```python run
# mod1.py
def add(a, b):
    return a + b

def sub(a, b):
    return a-b
```

```python run
import mod1
print(mod1.add(3,4)) # 7
```

import는 이미 만들어 놓은 파이썬 모듈을 사용할 수 있게 해주는 명령어이다.

```python run
from mod1 import add, sub # from mod1 import * -> 가능
add(3,4) # 7
```

위 형식을 사용하면 위와 같이 모듈 이름을 붙이지 않고 바로 해당 모듈의 함수를 쓸 수 있다.

### if **name** == "**main**":

```python run
# mod1.py
def add(a, b):
    return a+b

def sub(a, b):
    return a-b

print(add(1, 4))
print(sub(4, 2))
```

add(1, 4)와 sub(4, 2)의 결과를 출력하는 문장은 정상적으로 출력된다.
그러나 mod1.py 파일의 add와 sub 함수를 사용하기 위해
import mod1을 한다면 순간 mod1.py 파일이 실행되어 결괏값을 출력하게 된다.

```python run
# mod1.py
def add(a, b):
    return a+b

def sub(a, b):
    return a-b

if __name__ == "__main__":
    print(add(1, 4))
    print(sub(4, 2))
```

if **name** == "**main**"을 사용하면 직접 이 파일을 실행했을 때는 **name** == "**main**"이 참이 되어 if문 다음 문장이 수행된다.
반대로 대화형 인터프리터나 다른 파일에서 이 모듈을 불러서 사용할 때는 **name** == "**main**"이 거짓이 되어 if문 다음 문장이 수행되지 않는다.
