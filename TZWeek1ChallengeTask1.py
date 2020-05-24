def TZWeek1ChallengeTask1(nums, k, t):
    length = len(nums)    

    if nums[0] < 0 and nums[-1] > 0:
        if nums[-1] - nums[0] <= t:
            return True
        return False
    else:
        for i in range(length):
            num = nums[i]
            for j in range(k):
                if abs(nums[i+j]-num) <= t:
                    return True
                return False
  