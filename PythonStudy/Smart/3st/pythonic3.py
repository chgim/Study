import contextlib  # 컨텍스트 관리자와 관련된 기능을 제공하는 모듈

# try:
#     inasdfo
# except:
#     pass


# ValueError 예외를 억제하는 컨텍스트 블록을 엽니다.
# contextlib.suppress는 지정된 예외를 억제하는 컨텍스트 관리자를 생성합니다. 여기서는 ValueError가 억제됩니다.
with contextlib.suppress(ValueError):
    print("HH")  # HH"를 출력합니다.
    int("asdf")  # 이 부분에서는 ValueError가 발생합니다. 그러나 이 예외는 contextlib.suppress에 의해 억제됩니다.
    print("HH")  # 위의 예외로 인해 이 부분은 실행되지 않습니다.
# 결과적으로, 예외가 발생하더라도 ValueError는 억제되어 프로그램이 중단되지 않습니다. 대신, "HH"가 출력되고 프로그램이 계속 실행됩니다.


# C:\Users\kch11\Documents\GitHub\Study\PythonStudy\Smart>C:/Users/kch11/AppData/Local/Programs/Python/Python311/python.exe c:/Users/kch11/Documents/GitHub/Study/PythonStudy/Smart/3st/pythonic3.py
# HH
