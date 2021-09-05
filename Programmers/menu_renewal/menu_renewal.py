from itertools import combinations
from collections import Counter

#한 배열에 대한 조합을 해주는 combinations 모듈과 각 원소의 중복 갯수를 세주는 counter 모듈 사용
def solution(orders, course):
    answer = []
    #course에 들어있는 숫자 만큼 반복
    for c in course:
        temp = []
        for order in orders:
            #주문한 모든 메뉴들에 코스 숫자만큼 조합
            #중복 방지를 위해 정렬
            combi = combinations(sorted(order), c)
            temp += combi
        #해당 조합의 중복 갯수를 셈
        counter = Counter(temp)
        if len(counter) != 0 and max(counter.values()) != 1:
            #최댓값(현재 갯수에 해당하는 메뉴 조합 중 가장 많이 주문되었던 것) 을 가진 주문 조합을 다 넣음
            answer += [''.join(f) for f in counter if counter[f] == max(counter.values())]

    return sorted(answer)
