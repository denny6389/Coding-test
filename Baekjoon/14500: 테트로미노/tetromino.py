import sys;
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visit = [([0] * M) for _ in range(N)]
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
ans = 0
max_val = max(map(max, arr))

def dfs(r, c, idx, total):
    global ans
    #최대값과 선택할 수 있는 남은 블럭의 갯수만큼 (3 - idx) 곱해주고 현재 누적합 total 에 더해서 ans와 비교해주는 방식으로 가지치기
    if ans >= total + max_val * (3 - idx):
        return
    if idx == 3:
        ans = max(ans, total)
        return
    else:
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            #두번째 블럭을 선택했을 때 새로운 블럭에서 다음 블럭을 탐색하는 것이 아니라 다시 기존블럭에서 탐색하게 만들면 ㅗ모양을 만들 수 있다.
            if 0 <= nr < N and 0 <= nc < M and visit[nr][nc] == 0:
                if idx == 1:
                    visit[nr][nc] = 1
                    dfs(r, c, idx + 1, total + arr[nr][nc])
                    visit[nr][nc] = 0
                visit[nr][nc] = 1
                dfs(nr, nc, idx + 1, total + arr[nr][nc])
                visit[nr][nc] = 0

for r in range(N):
    for c in range(M):
        visit[r][c] = 1
        dfs(r, c, 0, arr[r][c])
        visit[r][c] = 0

print(ans)
