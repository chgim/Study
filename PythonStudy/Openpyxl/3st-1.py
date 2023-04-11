# 3 6 9 게임

# 1. 컴퓨터부터 입력을 시작합니다.

# 2. 박수는 space (띄어쓰기)로 입력합니다.

# 3. 컴퓨터는 10% 확률로 잘못된 값을 입력합니다.

#   - 1% 확률 => random.randint(1, 100) == 1

# 4. 잘못된 값을 입력하면 "컴퓨터 승리" 또는 "사용자 승리" 출력합니다.

import random 

count=0
while True:
    count+=1
    if '3' in str(count) or '6' in str(count) or '9' in str(count):
       answer=" "  * (str(count).count('3')+str(count).count('6')+str(count).count('9'))
    else:
        answer=count

    if random.randint(1,10)==1:
        print("사용자 승리")
        break
    else:
        print(f'컴퓨터:{answer}')    

    

    count+=1
    if '3' in str(count) or '6' in str(count) or '9' in str(count):
       answer=" "  * (str(count).count('3')+str(count).count('6')+str(count).count('9'))
    else:
        answer=str(count)
    human=input("사용자 입력:")
    if human!=answer:
        print("컴퓨터 승리")
        break
    else:
        pass
