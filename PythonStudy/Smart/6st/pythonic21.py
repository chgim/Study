from logging_decorator import logging_decorator


class CSVLoader:
    def __init__(self, filename):
        self._filename = filename

    @logging_decorator
    def load(self):
        with open(self._filename, "r", encoding="utf-8") as f:
            self._data = [int(line.strip()) for line in f.readlines()]

    @logging_decorator
    def analysis(self):
        print(self._data)
        print(sum(self._data))


csvloader = CSVLoader("test.csv")
csvloader.load()
csvloader.analysis()
