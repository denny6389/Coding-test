from itertools import combinations
import copy

N, M = map(int,input().split())
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
lab = []
infected = []
empty = []

for i in range(N):
    lab.append(list(map(int, input().split())))
    for j in range(M):
        if lab[i][j] == 0:
            empty.append((i, j))
        if lab[i][j] == 2:
            infected.append((i,j))

walls = list(combinations(empty,3))

def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 상, 하, 좌, 우 중에서 바이러스가 퍼질 수 있는 경우
        if nx >= 0 and nx < N and ny >= 0 and ny < M:
            if temp[nx][ny] == 0:
                # 해당 위치에 바이러스 배치하고, 다시 재귀적으로 수행
                temp[nx][ny] = 2
                virus(nx, ny)

safe = 0
for w in walls:
    temp = copy.deepcopy(lab)

    for i, j in w:
        temp[i][j] = 1

    for i, j in infected:
        virus(i, j)

    count = 0
    for m in temp:
        count += m.count(0)
    safe = max(safe, count)

print(safe)
