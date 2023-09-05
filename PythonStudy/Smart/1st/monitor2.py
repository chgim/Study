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