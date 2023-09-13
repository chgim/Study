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