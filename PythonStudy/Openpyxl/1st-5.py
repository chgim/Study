from openpyxl import load_workbook

wb = load_workbook('result.xlsx')
ws = wb.active # 마지막으로 열었던 Worksheet

print(ws['A1'].value)
print(ws['A:B'])
print(ws['1:2'])

for row in ws.iter_rows(values_only=True):
    print(row)