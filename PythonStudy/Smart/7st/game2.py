import random


class Game2:
    def make_user_answer(self):
        return input("가위?바위?보?")

    def make_computer_answer(self):
        answers = ["가위", "바위", "보"]
        return random.choice(answers)

    def check_result(self, answer1, answer2):
        if answer1 == answer2:
            return "비김"
        elif (
            (answer1 == "가위" and answer2 == "보")
            or (answer1 == "바위" and answer2 == "가위")
            or (answer1 == "보" and answer2 == "가위")
        ):
            return "승리"
        else:
            return "패배"

    def run_game(self):
        user = self.make_user_answer()
        computer = self.make_computer_answer()

        result = self.check_result(user, computer)
        print(result, computer)
        return result


if __name__ == "__main__":
    game = Game2()
    game.run_game
