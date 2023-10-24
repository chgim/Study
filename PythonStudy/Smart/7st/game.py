import random


def check_result(answer1, answer2):
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


# answers = ["가위", "바위", "보"]
# computer = random.choice(answers)

# user = input("가위?바위?보?")
# result = check_result(user, computer)
# print(result, computer)

# 가위바위보 게임 만들고 내가 가위를 냈을때 얼마나 패배하는지 알고싶을때 테스트 활용

# 추가
if __name__ == "__main__":
    answers = ["가위", "바위", "보"]
    computer = random.choice(answers)

    user = input("가위?바위?보?")
    result = check_result(user, computer)
    print(result, computer)
