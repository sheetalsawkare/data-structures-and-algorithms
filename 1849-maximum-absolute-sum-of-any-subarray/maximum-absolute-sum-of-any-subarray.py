class Solution:
    def maxAbsoluteSum(self, nums: list[int]) -> int:
        min_best=nums[0]
        max_best=nums[0]
        best=nums[0]
        res=nums[0]
        i=1
        while i<len(nums):
            v1=min_best+nums[i]
            v2=max_best+nums[i]
            v3=nums[i]
            min_best=min(v1, min(v2,v3))
            max_best=max(v1, max(v2,v3))
            best=max(abs(best), max(abs(min_best), abs(max_best)))
            res=max(res, best)
            i+=1
        return abs(res)