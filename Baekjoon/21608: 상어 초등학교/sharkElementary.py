import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())

dx = [-1,1,0,0]
dy = [0,0,-1,1]

# j,k 인덱스 자리에서 인접한 자리에 위치한 친구들 리스트와 빈칸의 수를 리턴하는 함수
# 한명의 학생이 앉을 자리를 선택하는 과정에서 빈자리를 모두 탐색해야하므로, 이때 빈칸인 j,k에 대해서 check함수를 호출
def check(j,k):
    near_list = []
    empty = 0
    for i in range(4):
        if j+dx[i] >=0 and j+dx[i] < n and k+dy[i] >=0 and k+dy[i] < n:
            if table[j+dx[i]][k+dy[i]]:
                near_list.append(table[j+dx[i]][k+dy[i]])
            else:
                empty += 1

    return near_list, empty

# 자리를 결정하는 함수
# l배열의 원소는 다음과 같다. (좋아하는 친구들 수, 빈칸의 수, 행, 열 )
# 이때 좋아하는 친구들이 많은 순 -> 빈칸이 많은 순 -> 행이 작은순 -> 열이 작은순 정렬해야하는데
# sorted()함수를 통해서 한번에 조건 4개를 모두 따지기위해서 (내림차순) 좋아하는 친구들수와 빈칸의수를 음수로해서 넣는다.
# 이렇게 하면 내림차순 정렬했을때 한번에 위 조건에 가장 부합하는 원소가 맨앞에 오게된다.
def find_seat(l):
    l = sorted(l, key=lambda x:(x[0], x[1], x[2], x[3]))
    cnt,emp,x,y = l[0]
    return x,y


student = defaultdict(list)

for _ in range(n*n):
    temp = list(map(int, input().split()))
    student[temp[0]] = temp[1:]

# 누군가 앉았다면 False에서 해당학생의 번호로 바꿔준다.
# 앉을 자리를 선택할때 table에서 False인 위치만 체크한다.
table = [[False] * n for _ in range(n)]

for i in student.keys():
    l = []
    temp = []
    cnt = 0
    like_friend = 0 # i가 앉을수있는 위치에서 좋아하는 친구들의 수
    for j in range(n):
        for k in range(n):
            if table[j][k]: # 누가 앉아있으면 건너뛰고
                continue
            #i학생이 j,k에 앉았을때 인접한 친구들과 인접한 빈칸의 수
            near_list, emp = check(j,k)

            for like in student[i]:
                if like in near_list:
                    cnt += 1
            temp.append(-cnt)
            temp.append(-emp)
            temp.append(j)
            temp.append(k)
            l.append(temp)
            temp = []
            cnt = 0

    # l- 친구리스트와 빈칸, 해당 자리
    x,y = find_seat(l)
    table[x][y] = i

answer = 0
score = {0:0, 1:1, 2:10, 3:100, 4:1000}

for i in range(n):
    for j in range(n):
        count = 0
        # i행 j열 자리의 인접한 칸에 있는 친구들을 불러와서
        friend_list = check(i,j)[0]
        for f in friend_list:
            # 그 친구들이 해당 자리에 앉아있는 사람의 좋아하는 사람 리스트 중에 있는 지 확인
            if f in student[table[i][j]]:
                count += 1
        # 만족도 계산
        answer += score[count]

print(answer)
