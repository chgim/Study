import datetime


class DateRangeIterable:
    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date
        self._current = start_date

    def __iter__(self):  # iter을 먼저 접근, 객체가 있으면 그 객체를 받아서 next 호출
        return self

    def __next__(self):
        if self._current > self.end_date:
            raise StopIteration()

        t = self._current
        self._current += datetime.timedelta(days=1)
        return t


start_date = datetime.date(2023, 10, 20)
# print(start_date + datetime.timedelta(days=2))
end_date = datetime.date(2023, 10, 26)
date_range = DateRangeIterable(start_date, end_date)


for date in date_range:
    print(date)


# print(next(date_range))
# print(next(date_range))
# print(next(date_range))

# a = iter(date_range)
# print(a)


# iterator = iter(date_range)
# next(iterator)
# next(iterator)
# next(iterator)
# next(iterator)
# next(iterator)

# C:\Users\kch11\Documents\GitHub\Study\PythonStudy\Smart>C:/Users/kch11/AppData/Local/Programs/Python/Python311/python.exe c:/Users/kch11/Documents/GitHub/Study/PythonStudy/Smart/4st/pythonic7.py
# 2023-10-20
# 2023-10-21
# 2023-10-22
# 2023-10-23
# 2023-10-24
# 2023-10-25
# 2023-10-26
