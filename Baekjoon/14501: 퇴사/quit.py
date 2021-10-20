import sys
input = sys.stdin.readline
N = int(input())
T = []
P = []
for i in range(N):
    a = list(map(int, input().split()))
    T.append(a[0])
    P.append(a[1])

D = [0] * N # 다이나믹 프로그래밍을 위한 1차원 DP 테이블 초기화

# 리스트를 뒤에서부터 거꾸로 확인
for i in range(N-1,-1,-1):
    if T[i] + i > N:
        D[i] = 0
    # 상담이 기간 안에 끝나는 경우
    else:
        if T[i]+i > (N-1):
            D[i] = P[i]
        else:
            index = T[i]+i
            D[i] = max(D[index:]) + P[i]

print(max(D))
