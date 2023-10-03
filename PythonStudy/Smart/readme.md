# 클린코드, 리팩토링, 코드리뷰

## 클린 코드 프로그래밍

- Flake8, Black Formatter(microsoft) 설치
- 보기-명령 팔레트-settings-기본 설정: 작업 영역 설정 열기(JSON)

## OOP(Object Oriented Programming) 객체 지향 프로그래밍

- 문제를 여러개의 객체 단위로 나눠 작업하는 방식으로, 객체들이 서로 유기적으로 상호작용하는 프로그래밍 이론
- JAVA, C#
- 클래스를 이용해 연관있는 함수와 변수를 하나의 인스턴스(객체)로 묶어 생성해 사용
- 캡슐화, 추상화, 상속성, 다형성
- 장점: 코드 재사용성, 생산성, 자연적인 모델링, 유지보수
- 단점: 개발속도, 설계에 많은 시간 소요, 실행속도 느림, 코딩 난이도 상승

## SOLID 원칙

- SRP(Single Responsibility Principle): 단일 책임 원칙
- OCP(Open Closed Priciple): 개방 폐쇄 원칙
- LSP(Listov Substitution Priciple): 리스코프 치환 원칙
- ISP(Interface Segregation Principle): 인터페이스 분리 원칙
- DIP(Dependency Inversion Principle): 의존 역전 원칙

## 단일 책임 원칙(SRP)

- 컴포넌트(클래스)는 단 하나의 책임을 가져야 함
- 만약, 필요 이상의 책임을 가진다면 =>신(God) 객체
- 단일 책임이 아닐 경우, 서로 다른 두 가지의 책임의 수정이 필요할때, 동일 컴포넌트가 수정
- 이 과정에서, 버그 발생이나 유지보수 어려워짐

### before: 보기 좋음, 수정하기 힘듬

```python run
class SystemMonitor:
    def load_activity(self):
        """시스템 활동 가져옴"""
    def stream_events(self):
        """이벤트를 외부로 전송"""
    def identify_events(self):
        """시스템 활동 해석 후 이벤트로 정의"""
```

### after: 수정하기 쉬움, 보기 안좋음

```python run
class ActivityWatcher:
    def load_activity(self):
        """시스템 활동 가져옴"""

class SystemMonitor:
    def identify_events(self):
        """시스템 활동 해석 후 이벤트로 정의"""

class Output:
    def stream_events(self):
        """이벤트를 외부로 전송"""
```

## 개방 폐쇄 원칙(OCP)

- 모듈이 개방, 폐쇄 되어있어야 하는 원칙
- 로직을 캡슐화 =>확장에는 개방, 수정에는 폐쇄
- 새로운 문제, 요구사항이 발생할 경우 기존 코드 유지, 새로운 코드를 추가할 수 있도록 구성

### before

```python run
class Event:
    """이벤트"""


class UnknownEvent(Event):
    """알수없는 이벤트"""


class LoginEvent(Event):
    """로그인 이벤트"""


class LogoutEvent(Event):
    """로그아웃 이벤트"""


class ShutdownEvent(Event):
    pass
```

```python run
from events import LoginEvent, LogoutEvent, UnknownEvent, ShutdownEvent


class SystemMonitor:
    event = 0

    def identify_event(self):
        if self.event == 0:
            return LoginEvent()
        elif self.event == 1:
            return LogoutEvent()
        elif self.event == 2:
            return ShutdownEvent()
        else:
            return UnknownEvent()
```

### after: 확장이 편함, SystemMonitor 코드에 오류가 생길 염려 X

```python run
class Event:
    """이벤트"""


class UnknownEvent(Event):
    @staticmethod
    def condition(value: int) -> bool:
        return False


class LoginEvent(Event):
    @staticmethod
    def condition(value: int) -> bool:
        return value == 0


class LogoutEvent(Event):
    @staticmethod
    def condition(value: int) -> bool:
        return value == 1


class ShutdownEvent(Event):
    @staticmethod
    def condition(value: int) -> bool:
        return value == 2
```

```python run
from events2 import Event, UnknownEvent


class SystemMonitor:
    event = 0

    def identify_event(self):
        for event_cls in Event.__subclasses__():
            if event_cls.condition(self.event):
                return event_cls()

        return UnknownEvent()


s = SystemMonitor()
print(s.identify_event())
```

## 리스코프 치환 원칙(LSP)

- 클래스의 하위 클래스을 그대로 사용할 수 있어야 하는 원칙
- 부모 타입 대신 어떠한 하위 타입도 사용할 수 있어야 함
- 부모 객체와 이를 상속한 자식 객체가 있을 때 부모 객체를 호출하는 동작에서 자식 객체가 부모 객체를 완전히 대체할 수 있다는 원칙
- 올바른 상속을 위해 자식 객체의 확장이 부모 객체의 방향을 올바르게 따르도록 권고
- 가급적 부모 객체의 일반 메소드를 그 의도와 다르게 오버라이딩 하지 않는것이 중요
- 부모 객체의 오버라이딩은 주로 동일한 메소드를 자식 객체만의 동작을 추가하기 위해 한다는 걸 감안하면 매우 준수하기 까다로운 원칙

```python run

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

```

## 인터페이스 분리 원칙(ISP)

- 인터페이스의 정의와 구현을 분리
  - 인터페이스는 객체가 노출하는 함수의 집합
  - 즉 함수의 정의와 구현을 분리
- 인터페이스를 작게 분리
  - SRP의 연장 내용: 가급적 적은 인터페이스를 갖도록
  - 가급적 작은 단위로 인터페이스를 분리
- in 파이썬
  - 함수의 형태를 보고 암시적으로 정의된다 => 덕 타이핑 원리

### isp.py

```python run

# ISP
# abc: Abstract Base Classes 추상 클래스
# 코드가 구체적인 구현에 의존하면 구현체가 바뀔때마다 무한 수정
from abc import ABCMeta, abstractmethod


class XMLEventParser(metaclass=ABCMeta):    # 인터페이스, 추상 메서드
    @abstractmethod
    def from_xml(self, xml_data: str):
        """xml을 분석하는 함수"""    # 주석


class EventParser(XMLEventParser):  # 구현체
    def from_xml(self, xml_data: str):
        print(xml_data)


class Event2Parser(XMLEventParser):  # 구현체
    def from_xml(self, xml_data: str):
        print(xml_data + "-2")


class Event3Parser(XMLEventParser):  # 구현체
    def from_xml(self, xml_data: str):
        print(xml_data + "-3")

# e = EventParser()
# e.from_xml("test")

# x = XMLEventParser()    # TypeError: Can't instantiate abstract class XMLEventParser with abstract method from_xml
# x.from_xml("test")

```

### is2.py

```python run

from isp import XMLEventParser


def analysis(parser: XMLEventParser):   # 구현체는 바뀔 수 있다. 개방 폐쇄의 원칙. 인터페이스만 바라봄
    parser.from_xml("t")


```

### is3.py

```python run

from isp2 import analysis
from isp import Event3Parser


e = Event3Parser()
analysis(e)

```

### 덕 타이핑(Duck Typing)

- '오리처럼 걷고, 오리처럼 꽥꽥거리면, 그것은 틀림없이 오리다.'
- 본질적으로 다른클래스라도 객체의 적합성은 객체의 실제 유형이 아니라 특정 메소드와 속성의 존재에 의해 결정

```python run

class Parrot:
    def fly(self):
        print("Parrot flying")

class Airplane:
    def fly(self):
        print("Airplane flying")

class Whale:
    def swim(self):
        print("Whale swimming")

def lift_off(entity):
    entity.fly()

parrot = Parrot()
airplane = Airplane()
whale = Whale()

lift_off(parrot) # prints `Parrot flying`
lift_off(airplane) # prints `Airplane flying`
lift_off(whale) # Throws the error `'Whale' object has no attribute 'fly'`

```

## 의존성 역전 원칙(DIP)

- 코드가 구체적인 구현에 의존하지 않고 인터페이스에 의존
  - 추상화를 통해 세부 사항에 의존하지 않도록 함
  - 세부 사항은 추상화에 의존
- A 함수가 B 클래스를 사용할 때
  - A 함수안에서 B 객체 생성 => A는 B에 의존
  - A 함수 안으로 B 객체 전달 => B가 A의 인터페이스(인자)에 의존
    - 의존성 주입(Dependency injection)

### before: 의존이 강함

```python run

from isp import EventParser, Event2Parser    # 의존이 강함


def test():
    e = EventParser()
    e.from_xml("test")


def test2():
    e = Event2Parser()
    e.from_xml("test")

```

```python run

from dip import test, test2


test()


test2()

```

### after: 의존성 주입

```python run

from isp import XMLEventParser


def test(e: XMLEventParser):    # 함수의 의존도 낮아짐, 함수의 활용도 높아짐
    e.from_xml("test")

```

```python run

from dip import test
from isp import Event2Parser


e = Event2Parser()
test(e)

```

### 예제 2

```python run

from abc import ABCMeta, abstractclassmethod


class AbstractLogger(metaclass=ABCMeta):
    @abstractclassmethod
    def send(data: str):
        """send data"""


class Logger(AbstractLogger):
    def send(self, data: str):
        print(data)


class FileLogger(AbstractLogger):
    def send(self, data: str):
        with open("output.log", "w") as f:
            f.write(data)
            f.close()


class EventStreamer1:
    def __init__(self):
        self._target = Logger()

    def stream(self, events: list) -> None:
        for ev in events:
            self._target.send(ev)


class EventStreamer2:
    def __init__(self, target: AbstractLogger):
        self._target = target

    def stream(self, events: list) -> None:
        for ev in events:
            self._target.send(ev)


e1 = EventStreamer1()
e1.stream({"1", "2", "3"})

e1 = EventStreamer2(FileLogger())
e1.stream({"1", "2", "3"})

```

## DRY / OAOO

- DRY: Do not Repeat Yourself
- OAOO: Once and Only Once
- 코드에 있는 기능 / 역할 / 지식은 단 한번, 한 곳에 정의
- 코드 중복시
  - 오류가 발생할 수 있다
  - 비용이 비싸다(시간이 더 소요)
  - 신뢰성 떨어짐
    => 즉 코드는 언제나 수정될 수 있는데, 이 과정을 거듭할 수록 문제가 커짐

## YAGNI

- YAGNI: You Ain't Gonna Need It
- 과잉 개발을 하기 위한 원칙
- 개발을 하다보면, 미래의 요구사항을 고려하기 마련
  - 수정사항에 대한 예상
  - 기능이 확장 될 것에 대한 예상
- 유지보수가 가능한 개발
  - 현재의 요구사항을 만족
  - 나중에 수정하기 쉽도록 작성하는것

## KIS

- KIS: Keep It Simple
- YAGNI와 유사
- 최대한 단순하게 작성/개발 (짧게 x 직관적 o)

## EAFP / LBYL

- EAFP: Easier to Ask Forgiveness than Permission
  - 일단 코드를 실행하고, 안될 때 대응
- LBYL: Look Before You Leap
  - 미리 검증이나 확인

## 계약에 의한 디자인

- 계약: 컴포넌트 간의 통신 중에 지켜야할 규칙
  - 사전 조건: 코드가 진행되기 전에 조건을 확인
  - 사후 조건: 호출한 코드가 컴포넌트로 부터 받은 값을 확인
  - 불변 속성(불변식): 코드가 실행되는 동안 유지되는 조건, 로직
    - 이러한 부분은 주석에 문서화 하는 것이 좋음
  - 부작용: 코드가 발생시킬 수 있는 부작용
    - 이러한 부분은 주석에 문서화 하는 것이 좋음

## 파이썬스러운 계약

- 코드를 실행하기 전 검사에 실패할 경우 예외 발생
  - RuntimeError, ValueError 등을 발생

## 방어적 프로그래밍

- 예상할 수 있는 오류를 처리 => Null, Exception
  - 값 대체(기본값 지정)
  - 빈 except 블록 지양
  - form e 를 사용한 원본 예외 포함
- 발생하지 않아야 하는 오류를 처리 => Assertion
  - assert 문법으로 검증.
  - AssertionError는 "발생하면 안되는" 오류 이므로, 프로그램을 종료

## Pythonic

- 클린 코드를 위한 여러 패턴, 기법 사용
  - 이러한 패턴, 기법 등은 언어와 무관한 고차원의 개념
  - 따라서 코드와 1:1로 즉시 변환되지 않음
- 클린 코드를 위한 패턴, 기법, 룰을 아는 것과 함께 언어의 관용구를 따르는 것도 중요

1. 인덱스와 슬라이스
2. 시퀀스 생성
3. 컨텍스트 관리자
4. 컴프리헨션
5. 프로퍼티, 속성
6. 이터러블 객체
7. 시퀀스

## 스크립트 언어 / 컴파일 언어

### 스크립트 언어

#### 정의

컴퓨터 프로그래밍 언어의 한 종류로, 스크립트 작성 기능을 지원하는 소프트웨어(애플리케이션)을 제어하는 역할을 하는 언어로 정의되어 있다. 수정이 자주 발생하는 덩치가 큰 소프트웨어에서 컴파일은 시간이 오래 소요되는 작업이므로, 수정이 빈번하게 발생하는 부분에서는 소스코드를 한줄씩 읽어 바로 실행하는 인터프리터 방식이 효율적이다. 이에 따라 스크립트 언어도 대부분 인터프리터 방식을 사용하는 인터프리터 언어라고 할 수 있다.

#### 특징

- 스크립트 언어는 컴파일 언어에 비해 단순하고 쉬운 문법 구조를 갖고 있다.
- 컴파일러 없이 명령어를 한줄씩 읽으면서 실행하므로, 번역속도는 빠르지만 프로그램 실행 시 매번 같은 코드를 번역해야 한다.
  따라서 프로그램의 실행속도는 컴파일 언어에 비해 느리다.
- CPU의 사용시간의 낭비가 크므로 복잡한 산술연산 혹은 복잡한 구조의 프로그램에서는 효율적이지 않을 수 있다.
- 컴파일 과정이 없기 때문에 프로그램을 실행시켜야 오류를 알 수 있다.
- 컴파일 과정이 없기 때문에, 소스 코드가 그대로 실행파일이 되어 메모리에 적재된다. 그 이후 런타임시 메모리가 명령어를 실행하기 위해
  내부적으로 기계어로 변환하는 과정을 거친다.
- ex: JavaScript, Python, JSP, jQuery 등

### 컴파일 언어

#### 정의

컴파일 언어란 소스코드(Source Code)를 컴파일 하여 목적코드(Object Code or Executable File)로 옮기고, 목적코드(기계어)를 읽어 실행시키는 방식으로 동작하는 언어이다.

#### 특징

- 문법적 제약이 많아, 스크립트 언어에 비해 사용이 어렵다.
- 컴파일을 하기 때문에 규모가 큰 프로그램일 경우 컴파일 하는데에 오랜 시간이 소요된다.
- 한번 컴파일을 하면, 이후에는 기계어를 읽어들이기 때문에 실행속도가 빠르다.
- 기계어를 통해 프로그램이 실행되기 때문에 프로그램의 소스코드가 유출되기 어렵다.
- O.S 마다 기계어가 상이하기 때문에 O.S에 따라 작업을 다르게 해주어야 한다.
- 컴파일러가 소스코드를 기계어로 변환시켜준다. 그 이후 기계어가 메모리에 적재된다.
- ex: C, C++, Java, Go 등
