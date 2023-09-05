
# OCP

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
