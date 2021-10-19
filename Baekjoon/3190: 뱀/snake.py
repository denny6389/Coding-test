from collections import deque
# 2차원 배열에서 오른쪽으로 갈려면 y(col)에서 +1, 왼쪽은 -1
# 2차원 배열에서 위로 갈려면 x(row)에서 -1, 아래는 +1
# 우, 하, 좌, 상

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def change(d, c):
    # 우(0) 하(1) 좌(2) 상(3)
    # 왼쪽 회전: 우(0) -> 상(3) -> 좌(2) -> 하(1) -> 우(0) : -1 방향
    # 오른쪽 회전: 우(0) -> 하(1) -> 좌(2) -> 상(3) -> 우(0) : +1 방향
    if c == "L":
        d = (d - 1) % 4
    else:
        d = (d + 1) % 4
    return d


def start():
    direction = 0  # 초기 방향: 우(0)
    time = 1  # 시간
    x, y = 0, 0  # 초기 뱀 위치: 맨위 맨좌측
    visited = deque([[x, y]])  # 방문한 위치
    arr[x][y] = 2
    while True:
        x, y = x + dx[direction], y + dy[direction]
        # 위치가 보드 게임 내에 있고 자기 자신 몸이 아닌 경우
        if 0 <= y < N and 0 <= x < N and arr[x][y] != 2:
            if not arr[x][y] == 1:  # 사과가 없는 경우
                temp_x, temp_y = visited.popleft()
                arr[temp_x][temp_y] = 0  # 꼬리 제거
            # 방문한 위치 체크
            arr[x][y] = 2
            visited.append([x, y])
            # 방향 변환
            if time in times.keys():
                direction = change(direction, times[time])
            time += 1
        else:  # 본인 몸에 부딪히거나, 벽에 부딪힌 경우
            return time


N = int(input())
K = int(input())

# 2차원 배열 생성: 0으로 초기화
arr = [[0] * N for _ in range(N)]

# 사과 위치
for _ in range(K):
    a, b = map(int, input().split())
    arr[a - 1][b - 1] = 1  # 사과 저장
# 방향 변환 정보
L = int(input())
times = {}
for i in range(L):
    X, C = input().split()
    times[int(X)] = C
print(start())
