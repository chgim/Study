from openpyxl import Workbook

wb = Workbook()# 데이터를 쓸 클래스 변수 생성 (파일명 없이)
ws = wb.active # 마지막으로 열었던 Worksheet

for i in range(10): # 0~9
    ws.append([i, f'{i} Data']) # 액셀 파일에 데이터 추가

wb.save('result.xlsx') 