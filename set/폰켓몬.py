def solution(nums):
    num_set = set(nums) #nums 리스트에서 중복 제거한 집합
    n = len(nums) #폰켓몬의 총 개수
    k = n // 2 #선택할 폰켓몬의 수
    return min(k, len(num_set))
    #중복을 제거한 폰켓몬 수와 선택할 폰켓몬 수 중 작은 값 반환