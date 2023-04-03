from openpyxl import Workbook

wb = Workbook()
ws = wb.active # 마지막으로 열었던 Worksheet

for i in range(10):
    ws.append([i, f'{i} Data'])
wb.save('result.xlsx')