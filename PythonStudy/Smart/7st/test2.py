import unittest
from unittest.mock import MagicMock
from game2 import (
    Game2,
)  # from import를 한다면 무조건 check_result 함수를 한번 실행. 그래서 해당 함수와 테스트 코드가 같이 동작


class Test2(unittest.TestCase):
    def test_num(self):  # 테스트 하고 싶은 함수는 test_로 시작해야 자동으로 인식하고 테스트 해줌
        game = Game2()
        game.make_user_answer = MagicMock(return_value="가위")
        game.make_computer_answer = MagicMock(return_value="보")
        result = game.run_game()
        self.assertEqual(result, "승리")


if __name__ == "__main__":
    unittest.main()
