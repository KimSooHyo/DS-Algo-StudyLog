"""
(target - arr의 특정 원소)를 키로 갖는 값이 있으면 target이 되는 경우가 있는 것

- 직접 다 더해보는 방식은 O(n^2)으로 비효율적
"""

def solution(arr, target):
    hash = [0] * (target + 1) #해시 테이블 생성 및 초기화
    
    #arr의 각 원소를 키로 해시 테이블을 만듦
    for num in arr:
        if num <= target:
            hash[num] = 1
    
    for num in arr:
        #target보다 크면 답이 될 수 없음
        if (num > target):
            continue
        
        # 같은 수를 두 번 쓰면 안 되므로 패스
        if ((target - num) == num):
            continue
        
        #두 수의 합으로 target 만들 수 있으면 True
        if (hash[target - num]):
            return True
    #두 수의 합으로 target을 만들 수 없으면 False
    return False