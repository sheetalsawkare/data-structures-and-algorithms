class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        min_sum=nums[0]
        max_sum=nums[0]
        current_max=nums[0]
        current_min=nums[0]
        sum=nums[0]
        i=1
        while i<len(nums):
            current_min=min(nums[i],nums[i]+current_min)
            min_sum=min(min_sum, current_min)
            current_max=max(nums[i],nums[i]+current_max)
            max_sum=max(max_sum, current_max)
            sum+=nums[i]
            i+=1
        circular = sum - min_sum
        answer = max(circular, max_sum)
        if max_sum < 0:
            return max_sum
        else:
            return answer