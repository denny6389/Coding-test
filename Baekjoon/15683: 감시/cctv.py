import copy
INF = int(1e9)

# 동 서 남 북
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
# 각 CCTV가 감시하는 방향을 회전하는 것을 포함해서 direction이라는 변수에 담아둔다.
direction = [[], [[0], [1], [2], [3]], [[0, 1], [2, 3]], [[0, 2], [2, 1], [1, 3], [3, 0]],[[3, 0, 2], [1, 3, 0], [0, 2, 1], [2, 1, 3]], [[0, 1, 2, 3]]]

n, m = map(int, input().split())
office = []
cctv_cnt = 0
q = []
ans = INF
for i in range(n):
    input_data = list(map(int, input().split()))
    office.append(input_data)
    for j in range(len(input_data)):
        if input_data[j] != 0 and input_data[j] != 6:
            # 입력을 받을 때는 CCTV의 개수를 구해놓고, 해당 CCTV의 좌표와 번호를 큐에 담아준다.
            cctv_cnt += 1
            q.append([i, j, input_data[j]])

def watch(y, x, direct, tmp):
    for d in direct:
        nx = x
        ny = y
        while True:
            nx += dx[d]
            ny += dy[d]
            if nx >= 0 and nx < m and ny >= 0 and ny < n and tmp[ny][nx] != 6:
                if tmp[ny][nx] == 0:
                    tmp[ny][nx] = '#'
            else:
                break

def dfs(office, cnt):
    global ans
    tmp = copy.deepcopy(office)
    if cnt == cctv_cnt:
        c = 0
        for i in tmp:
            c += i.count(0)
        ans = min(ans, c)
        return
    y, x, cctv = q[cnt]
    for i in direction[cctv]:
        watch(y, x, i, tmp)
        dfs(tmp, cnt + 1)
        tmp = copy.deepcopy(office)

dfs(office, 0)
print(ans)
