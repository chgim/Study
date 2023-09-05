# 클린 코드 프로그래밍
- Flake8, Black Formatter(microsoft) 설치
- 보기-명령 팔레트-settings-기본 설정: 작업 영역 설정 열기(JSON)

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