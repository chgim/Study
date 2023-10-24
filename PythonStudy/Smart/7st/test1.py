import unittest
from game import (
    check_result,
)  # from import를 한다면 무조건 check_result 함수를 한번 실행. 그래서 해당 함수와 테스트 코드가 같이 동작


class Test1(unittest.TestCase):
    def setUp(self):
        print("setUp")

    def tearDown(self):
        print("tearDown")

    def test_num(self):  # 테스트 하고 싶은 함수는 test_로 시작해야 자동으로 인식하고 테스트 해줌
        print("num1")
        user = "가위"
        computer = "바위"
        result = check_result(user, computer)
        self.assertEqual(result, "패배")

    def test_num2(self):  # 테스트 하고 싶은 함수는 test_로 시작해야 자동으로 인식하고 테스트 해줌
        print("num2")
        user = "바위"
        computer = "가위"
        result = check_result(user, computer)
        self.assertEqual(result, "승리")

    def test_num3(self):  # 테스트 하고 싶은 함수는 test_로 시작해야 자동으로 인식하고 테스트 해줌
        print("num3")
        user = "보"
        computer = "바위"
        result = check_result(user, computer)
        self.assertEqual(result, "승리")

    def num4(self):  # 테스트 하고 싶은 함수는 test_로 시작해야 자동으로 인식하고 테스트 해줌
        user = "바위"
        computer = "가위"
        result = check_result(user, computer)
        self.assertEqual(result, "승리")


if __name__ == "__main__":
    unittest.main()
