try:
    int("adsds")
# except:  # 위험한 프로그래밍
#     pass
except ValueError as e:
    # print("ValueError", e)
    raise RuntimeError("Runtime Error!~") from e
