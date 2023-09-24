class BackupHandler:  # start를 보장
    def __enter__(self):
        print("Stop db")
        return self

    def __exit__(self, exc_type, ex_value, ex_traceback):
        print(exc_type)
        print(ex_value)
        print(ex_traceback)
        print("Start db")

    def backup(self):
        print("Backup db")


with BackupHandler() as handler:
    raise RuntimeError("my message")
    handler.backup()

# with open("dip.py", "r") as f:  # contaxt manager
#     print(f.read())
#     raise TypeError


# f = open("output.txt", "w")
# f.write("test")

# raise Exception

# f.close()
