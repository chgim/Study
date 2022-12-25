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

### 문자열 슬라이싱

a[시작 번호:끝 번호] -> 끝 번호는 포함 X

```python run
a = "Life is too short, You need Python"
print(a[0:4]) # 'Life'
```

### 문자열 관련 함수

count, find, index, join, upper, lower, lsrtip, rstrip, strip, replace, split
