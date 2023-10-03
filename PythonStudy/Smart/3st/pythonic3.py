import contextlib

# try:
#     inasdfo
# except:
#     pass

with contextlib.suppress(ValueError):
    print("HH")
    int("asdf")
    print("HH")
