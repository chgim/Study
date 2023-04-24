f = open('test.txt', 'r', encoding='utf-8') # text.txt 파일을 읽기 모드로 열기 
print(f.read()) # f 파일을 읽고 프린트
f.close() # f 파일 닫기

# encoding: 파일을 읽을 때 사용할 문자 해석 방법
# utf-8: 윈도우를 제외하고 많이 일반적으로 쓰이는 방법