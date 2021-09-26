import sys
input = sys.stdin.readline
H, W = map(int,input().split())
block = list(map(int,input().split()))
answer = 0

'''
양쪽에 더 높은 블록이 존재하면 빗물이 고인다.

따라서 반복문을 돌며 현재 블록의 왼쪽 값 중 최대높이, 오른쪽 값 중 최대높이를 구해

그 두 값중 작은 값이 현재 블록높이보다 크다면, 큰 값은 당연히 블록높이보다 크므로

작은 값 - 현재 블록 높이를 ans에 더해준다.
'''
for i in range(1, W-1):
    left = max(block[ :i])
    right = max(block[i+1: ])
    m = min(left, right)
    # 좌우의 블럭 높이의 최댓값 중 작은 값이 현재 블록보다 크다면
    # 반대쪽 값도 그 블럭보다 크다. 따라서 작은 값 - 현재블럭 높이 만큼 ans에 저장.
    if m > block[i]:
        answer += m - block[i]
 
print(answer)
