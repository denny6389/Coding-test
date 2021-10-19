from itertools import combinations

N, M = map(int, input().split())

house = []
chicken = []

for r in range(N):
    row = list(map(int, input().split()))
    for c in range(len(row)):
        if row[c] == 1:
            house.append((r, c)) # 일반 집
        elif row[c] == 2:
            chicken.append((r, c)) # 치킨 집

# 모든 치킨집 중에서 m개의 치킨집을 뽑는 조합 계산
candidates = combinations(chicken, M)

# 치킨 거리의 합을 계산하는 함수
def simulate(candidate):
    result = 0
    for h in house:
        temp = 1e9
        for cand in candidate:
            distance = abs(h[0]-cand[0]) + abs(h[1]-cand[1])
            temp = min(temp, distance)
        # 가장 가까운 치킨집까지의 거리를 더하기
        result += temp
    # 치킨 거리의 합 반환
    return result

# 치킨 거리의 합의 최소를 찾아 출력
answer = 1e9
for candidate in candidates:
    distance = simulate(candidate)
    answer = min(answer, distance)

print(answer)
