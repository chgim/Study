from openpyxl import Workbook

wb = Workbook()
ws = wb.active # 마지막으로 열었던 Worksheet

ws['A1'] = 'Test Data!'
wb.save('result.xlsx')


# python -m venv venv
# TERMINAL-> Command Prompt-> pip install openpyxl