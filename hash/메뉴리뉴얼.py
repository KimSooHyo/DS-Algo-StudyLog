from itertools import combinations
from collections import Counter
def solution(orders, course):
    answer = []
    
    for c in course: #각 코스 요리 길이에 대해
        menu = []
        
        for order in orders: #모든 주문에 대해
            comb = combinations(sorted(order), c) #조합을 이용해 가능한 메뉴 구성 구함
            menu += comb
        
        counter = Counter(menu) #각 메뉴 구성 몇 번 주문되었는지
        if len(counter) != 0 and max(counter.values()) != 1: #가장 많이 주문된 구성이 1번 이상인 경우
            for m, cnt in counter.items():
                if cnt == max(counter.values()): #가장 많이 주문된 구성 찾음
                    answer.append("".join(m)) #정답 리스트에 추가
                    
    return sorted(answer) #오름차순 정렬 후 반환