# 스무고개 게임 숫자 맞추기

# 1. 컴퓨터가 랜덤으로 1 ~ 100 사이의 수를 생성
# 2. 총 10번의 기회동안 숫자를 맞추는 게임
# 3. 사용자가 입력한 값이 숫자가 아니거나, 1 ~ 100 사이의 수가 아니라면
#    기회 차감 X
# 4. 사용자가 입력한 값에 따라서 컴퓨터는 Up/Down 을 출력
# 5. 아래와 같은 메뉴 출력
#     1) 게임 시작
#     2) 게임 종료
# 6. 메뉴에서 1,2를 입력 받고 게임 시작을 선택하면 반복해서 게임 가능
# 게임결과: 성공, 실패
# 7. 메뉴 변경
#       1) 게임 시작
#       2) 기록 보기
#       3) 게임 종료

import random

def start_game():
    status = "실패" # status는 실패로 시작. 성공 시에는 status를 성공으로 교체함.
    num = random.randint(1, 100) # 1~100 사이의 랜덤 값 생성성
    chance = 10 # 기회는 10번
    while chance > 0: # 기회가 0보다 클 때까지
        chance -= 1 # 기회 -1

        user_input = input('1~100 사이를 입력하세요:') # 유저에게 1~100 사이의 값 입력받음
        if not user_input.isdigit() or int(user_input) < 0 or int(user_input) > 100: # 숫자가 아니거나 입력 값이 0보다 작거나, 100보다 큰 경우 -> 입력 값은 문자형이기 때문에 int 형으로 변환하여 비교 
            chance += 1 # 기회차감을 하지 않기로 약속되어 있기에 -1 했던 기회를 다시 +1 해줌
            continue # 다시 while문 처음으로 돌아감

        user_input = int(user_input) # 입력 값은 문자형이기 때문에 int 형으로 변환
        if user_input == num: # 정답을 맞추었을 경우
            status = "성공" # status를 성공으로 교체
            print("정답!") # 정답 프린트
            break # 함수 나가기
        elif user_input < num: # 정답보다 작게 입력 시 
            print("UP") # up 출력
        elif user_input > num: # 정답보다 크게 입력 시 
            print("DOWN") # down 출력

    return status # status 값 반환

results = [] # results라는 리스트 자료형 선언
menu = ''
while menu != '3': # 게임 종료를 선택하기 전까지는 무한루프
    print("1) 게임 시작")
    print("2) 기록 보기")
    print("3) 게임 종료")
    menu = input('메뉴 선택:') # 메뉴 선택 입력받음
    if menu == '1': # 게임 시작 버튼 누를 시 
        result = start_game() # result에 start_game 함수의 반환 값 받아옴
        results.append(result) # results(리스트)에 result 값을 추가 [x,x,x,x] 
    elif menu == '2': # 기록 보기 버튼 누를 시 
        print(", ".join(results)) # results 리스트 안에 있는 값들을 ","라는 구분자와 join을 통해 합쳐서 출력

# - ''.join(리스트)
# ''.join(리스트)를 이용하면 매개변수로 들어온 ['a', 'b', 'c'] 이런 식의 리스트를 'abc'의 문자열로 합쳐서 반환해주는 함수

# - '구분자'.join(리스트)
# '구분자'.join(리스트)를 이용하면 리스트의 값과 값 사이에 '구분자'에 들어온 구분자를 넣어서 하나의 문자열로 합쳐줍니다.
# '_'.join(['a', 'b', 'c']) 라 하면 "a_b_c" 와 같은 형태로 문자열을 만들어서 반환해 줍니다.