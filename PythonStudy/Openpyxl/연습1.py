# 카카오 신입 공채 2022 신고 결과 받기

# 신입사원 무지는 게시판 불량 이용자를 신고하고 처리 결과를 메일로 발송하는 시스템을 개발하려 합니다. 무지가 개발하려는 시스템은 다음과 같습니다.

# 각 유저는 한 번에 한 명의 유저를 신고할 수 있습니다.
# 신고 횟수에 제한은 없습니다. 서로 다른 유저를 계속해서 신고할 수 있습니다.
# 한 유저를 여러 번 신고할 수도 있지만, 동일한 유저에 대한 신고 횟수는 1회로 처리됩니다.
# k번 이상 신고된 유저는 즉시 게시판 이용이 정지되며, 해당 유저를 신고한 모든 유저에게 정지 사실을 메일로 발송합니다.
# 게시판 이용이 정지된 유저도 불량 이용자를 신고할 수 있습니다.
 

# 다음은 전체 유저 목록이 [“muzi”, “frodo”, “apeach”, “neo”]이고, k = 2(즉, 2번 이상 신고 당하면 이용 정지)인 경우의 예시입니다.

# 유저 ID	신고 ID	설명
# “muzi”	“frodo”	“muzi”가 “frodo”를 신고했습니다.
# “apeach”	“frodo”	“apeach”가 “frodo”를 신고했습니다.
# “frodo”	“neo”	“frodo”가 “neo”를 신고했습니다.
# “muzi”	“neo”	“muzi”가 “neo”를 신고했습니다.
# “apeach”	“muzi”	“apeach”가 “muzi”를 신고했습니다.

# 각 유저별로 신고 당한 횟수는 다음과 같습니다.

# 유저 ID	신고 당한 횟수
# “muzi”	1
# “frodo”	2
# “apeach”	0
# “neo”	2
# 위 예시에서는 2번 이상 신고당한 “frodo”와 “neo”의 게시판 이용이 정지됩니다. 이때, 각 유저별로 신고한 아이디와 정지된 아이디를 정리하면 다음과 같습니다.

# 유저 ID	신고 ID	정지 ID
# “muzi”	[“frodo”, “neo”]	[“frodo”, “neo”]
# “frodo”	[“neo”]	[“neo”]
# “apeach”	[“muzi”, “frodo”]	[“frodo”]
# “neo”	없음	없음
# 따라서 “muzi”는 처리 결과 메일을 2회, “frodo”와 “apeach”는 각각 처리 결과 메일을 1회 받게 됩니다.

# 이용자의 id가 담긴 문자열 배열 id_list, 각 이용자가 신고한 이용자에 대한 정보가 담긴 문자열 배열 report, 정지 기준이 되는 신고 횟수 k가 매개변수로 주어질 때, 각 유저별로 처리 결과 메일을 받은 횟수를 배열에 담아 return 하도록 solution 함수를 완성해 주세요.

# 입출력 예

# id_list	report	k	result
# ["muzi", "frodo", "apeach", "neo"]	["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]	2	[2,1,1,0]
# ["con", "ryan"]	["ryan con", "ryan con", "ryan con", "ryan con"]	3	[0,0]

id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2

reports={"muzi":[],"frodo":[],"apeach":[],"neo":[]}
count={"muzi":0,"frodo":0,"apeach":0,"neo":0}

for rows in report:
    src, dest=rows.split(' ')
    reports[dest].append(src)
for name in id_list:
    if len(reports[name])>=k:
        for target in reports[name]:
            count[target]+=1
result=[]
for name in id_list:
    result.append(count[name])
print(result)








# def solution(id_lists, report,k):
#     answer = [0]*len(id_lists)
#     reports = {x:0 for x in id_lists}

#     for r in set(report):
#         reports[r.split()[1]] +=1

#     for r in set(report):
#         if reports[r.split()[1]] >= k:
#             answer[id_lists.index(r.split()[0])] +=1

#     print(answer)
#     return answer



# solution(["muzi", "frodo", "apeach", "neo"]	,["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]	,2)
