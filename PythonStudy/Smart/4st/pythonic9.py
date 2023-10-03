class Boundaries:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __contains__(self, coord):  # 매직 메서드. in과 연결
        x, y = coord  # 언패킹. 리스트를 받아와서 쪼개서 넣음
        return 0 <= x < self.width and 0 <= y < self.height  # 파이썬은 범위에 대한 조건을 이와 같이 가능


b = Boundaries(100, 200)

if [10, 20] in b:
    print("Hello")
