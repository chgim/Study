import datetime


class DateRangeSequence:
    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date

    def __getitem__(self, index):
        current = self.start_date + datetime.timedelta(days=index)

        if current > self.end_date:
            raise IndexError()

        return current


start_date = datetime.date(2023, 10, 1)
# print(start_date + datetime.timedelta(days=2))
end_date = datetime.date(2023, 10, 3)
date_range = DateRangeSequence(start_date, end_date)


print(date_range[0])

for date in date_range:
    print(date)

# C:\Users\kch11\Documents\GitHub\Study\PythonStudy\Smart>C:/Users/kch11/AppData/Local/Programs/Python/Python311/python.exe c:/Users/kch11/Documents/GitHub/Study/PythonStudy/Smart/4st/pythonic8.py
# 2023-10-01
# 2023-10-01
# 2023-10-02
# 2023-10-03
