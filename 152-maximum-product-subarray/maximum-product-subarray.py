class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        min_best=nums[0]
        max_best=nums[0]
        res=nums[0]
        i=1
        while i<len(nums):
            v1=nums[i]
            v2=min_best*nums[i]
            v3=max_best*nums[i]
            min_best=min(v1, min(v3,v2))
            max_best=max(v1, max(v2,v3))
            res = max(res, max(min_best, max_best))
            i+=1
        return res