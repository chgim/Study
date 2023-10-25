# 컨텍스트 관리자
# 컨텍스트 관리자는 with 키워드를 사용하여 블록 내에서 어떤 작업을 시작하고 끝내기 위해 사용


class BackupHandler:  # start를 보장
    # 컨텍스트가 시작될 때 호출되는 메서드입니다. 이 메서드는 컨텍스트 내에서 수행될 초기화 작업을 담습니다.
    def __enter__(self):
        print("Stop db")
        return self

    # 컨텍스트가 종료될 때 호출되는 메서드입니다. 이 메서드는 컨텍스트가 종료될 때 정리 작업을 담습니다.
    def __exit__(self, exc_type, ex_value, ex_traceback):
        print(exc_type)
        print(ex_value)
        print(ex_traceback)
        print("Start db")

    def backup(self):
        print("Backup db")


# 컨텍스트 블록을 열고, BackupHandler 클래스의 인스턴스를 handler 변수에 할당
# 파일이나 소켓 연결을 열었을 때 할당된 리소스를 모두 해제해주어야 하는데, 이 때 생각하지 못한 예외나 오류가 발생할 수도 있다. with 문 사용. 블록의 마지막이 실행되고 나면 컨텍스트가 종료되며, 예외가 발생한 경우에도 블록이 완료되면 파일이 자동으로 닫히게 됩니다.
with BackupHandler() as handler:
    # 이 예외가 발생하면 컨텍스트 블록 내의 코드는 중단되고 예외 정보가 __exit__ 메서드로 전달
    raise RuntimeError("my message")
    handler.backup()

# with open("dip.py", "r") as f:  # contaxt manager
#     print(f.read())
#     raise TypeError


# f = open("output.txt", "w")
# f.write("test")

# raise Exception

# f.close()
