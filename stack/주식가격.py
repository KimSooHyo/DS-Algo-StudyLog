def solution(prices):
    n = len(prices)
    answer = [0] * n # 기간 저장할 배열
    
    #스택을 사용해 이전 가격과 비교
    stack = [0]
    for i in range(1, n):
        while stack and prices[i] < prices[stack[-1]]:
            #가격이 떨어짐
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)
    # 스택에 남아있는 가격은 가격이 떨어지지 않은 경우
    while stack:
        j = stack.pop()
        answer[j] = n - 1 - j
    return answer