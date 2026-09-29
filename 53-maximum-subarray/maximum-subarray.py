class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        best=nums[0]
        res=nums[0]
        i=1
        while i<len(nums):
            v1=best+nums[i]
            v2=nums[i]
            best=max(v1,v2)
            res=max(best,res)
            i+=1

        return res