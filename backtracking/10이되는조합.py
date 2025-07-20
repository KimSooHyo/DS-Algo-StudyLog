"""
- results : 최종 반환 값
- sum : 현재까지 선택한 숫자들의 합
- selected_nums : 현재까지 선택된 숫자들을 담고 있는 리스트
- start : 다음에 선택할 숫자의 시작값을 지정해 주는 인자
"""

def backtrack(sum, selected_nums, start, N, results):
    if sum == 10: #합이 10이 되면 결과 리스트에 추가
        results.append(selected_nums)
        return
    for i in range(start, N+1): #다음에 선택할 수 있는 숫자들을 하나씩 선택하면서
        if sum + i <= 10: #선택한 숫자의 합이 10보다 작거나 같으면
            backtrack(
                sum + i, selected_nums + [i], i+1, results
            ) #백트래킹 함수를 재귀적으로 호출
        
def solution(N):
    results = [] #조합 결과를 담을 리스트
    backtrack(0, [], 1, N, results) #백트래킹 함수 호출
    return results #조합 결과 반환