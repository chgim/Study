# 문제
# 3 6 9 게임

# 1. 컴퓨터부터 입력을 시작합니다.

# 2. 박수는 space (띄어쓰기)로 입력합니다.

# 3. 컴퓨터는 10% 확률로 잘못된 값을 입력합니다.

#   - 1% 확률 => random.randint(1, 100) == 1

# 4. 잘못된 값을 입력하면 "컴퓨터 승리" 또는 "사용자 승리" 출력합니다.

# 정답
import random # random 함수를 사용하기 위해 random 모듈 임포트 해오기

count=0 # 첫 카운트 시작은 0으로 시작.

while True: # while문 무한 반복 ( 특정 조건을 충족 시켜야 나갈 수 있음 ex) break )

    # 컴퓨터 차례
    count+=1 # count 변수 값 1 증가 
    if '3' in str(count) or '6' in str(count) or '9' in str(count): # 만약 count 값에 '3', '6', '9' 중 하나의 문자라도 있다면 (문자열과 비교하기 위해 str(count)로 변환)  
       answer=" "  * (str(count).count('3')+str(count).count('6')+str(count).count('9')) # count에서 '3','6','9'의 개수만큼 answer에 " "(띄어쓰기) 대입. ex)33->" "" " 
    else: # 아닐 경우
        answer=count # answer에 count 값 대입

    if random.randint(1,100)==1: # 1부터 100 사이의 임의의 정수 값이 1이 나올 경우 (1% 확률로)
        print("사용자 승리") # 사용자 승리 출력
        break # while문 나가기 (프로그램 종료)
    else: # 아닐 경우
        print(f'컴퓨터:{answer}') # 컴퓨터의 answer 값 가져와서 출력   

    # 사용자 차례
    count+=1 # 카운트 변수 값 1 증가
    if '3' in str(count) or '6' in str(count) or '9' in str(count): # 만약 count 값에 '3', '6', '9' 중 하나의 문자라도 있다면 (문자열과 비교하기 위해 str(count)로 변환)  
       answer=" "  * (str(count).count('3')+str(count).count('6')+str(count).count('9'))  # count에서 '3','6','9'의 개수만큼 answer에 " "(띄어쓰기) 대입. ex)33->" "" " 
    else: # 아닐 경우
        answer=str(count) # answer에 str로 변환한 count 값 대입(사용자의 입력은 문자열로 받기 때문)
    
    human=input("사용자 입력:") # 사용자 입력 받고 human 변수에 저장.(문자열 형태임)

    if human!=answer: # 만약 human 과 answer의 값이 일치하지 않는다면(사용자 입력과 answer 값이 불일치)
        print("컴퓨터 승리") # 컴퓨터 승리 출력
        break  # while문 나가기 (프로그램 종료)
    else: # 아닐 경우
        pass # 넘어간다(다음 컴퓨터 차례)
