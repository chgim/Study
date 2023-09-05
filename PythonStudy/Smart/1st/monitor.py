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