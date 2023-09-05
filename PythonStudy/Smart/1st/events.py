# SRP

# class SystemMonitor:
#     def load_activity(self):
#         """시스템 활동 가져옴"""
#     def stream_events(self):
#         """이벤트를 외부로 전송"""
#     def identify_events(self):
#         """시스템 활동 해석 후 이벤트로 정의"""


# class ActivityWatcher:
#     def load_activity(self):
#         """시스템 활동 가져옴"""


# class SystemMonitor:
#     def identify_events(self):
#         """시스템 활동 해석 후 이벤트로 정의"""


# class Output:
#     def stream_events(self):
#         """이벤트를 외부로 전송"""

# OCP

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
