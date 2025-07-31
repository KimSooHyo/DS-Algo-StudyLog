def solution(n):
    answer = 0
    nums = [0] * (n+1)
    nums[1] = 1
    for i in range(2, n+1):
        nums[i] = (nums[i-2] + nums[i-1])%1234567
        
    return nums[n]