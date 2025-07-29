def lis(nums):
    n = len(nums)
    
    #dp[i]는 nums[i]를 마지막으로 하는 lis의 길이를 저장하는 배열
    dp = [1] * n
    
    for i in range(1, n):
        for j in range(i):
            #nums[i]와 nums[j]를 비교하여, nums[i]가 더 큰 경우에만 처리
            if nums[i] > nums[j]:
                #nums[i]를 이용하여 만든 부분 수열의 길이와
                #nums[j]를 이용하여 만든 부분 수열의 길이 +1 중 최댓값을 저장
                dp[i] = max(dp[i], dp[j]+1)
                
    return max(dp)