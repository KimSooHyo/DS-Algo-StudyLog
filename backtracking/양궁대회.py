"""
어떻게 해야 모든 경우를 빠지지 않고 체크할 수 있을까
-> 조합을 생각해야 함
"""
#복원 조합
from itertools import combinations_with_replacement
from collections import Counter

#주어진 조합에서 각각의 점수 계산
def calculate_score(combi, info):
    score1, score2 = 0,0
    for i in range(1, 11):
        if info[10-i] < combi.count(i):
            score1 += i
        elif info[10-i] > 0:
            score2 += i
    return score1, score2

#최대 차이와 조합 저장
def calculate_best_combination(n, info):
    max_diff = 0
    max_comb = {}
    
    for combi in combinations_with_replacement(range(11), n): #모든 중복 조합
        cnt = Counter(combi) #각 점수에 몇 발 쐈는지
        score1, score2 = calculate_score(combi, info)
        diff = score1 - score2
        
        if diff > max_diff:
            max_diff = diff
            max_comb = cnt
    
    return max_diff, max_comb

#결과 반환
def solution(n, info):
    max_diff, max_comb = calculate_best_combination(n, info)
    
    if max_diff > 0:
        answer = [0] * 11
        for score in max_comb: #리스트 형태의 조합 결과
            answer[10 - score] = max_comb[score]
        return answer
    else:
        return [-1]