class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n=len(nums)
        i=0
        res = []

        while i<n-2:
            left=i+1
            right=n-1

            if i>0 and nums[i]==nums[i-1]:
                i+=1
                continue
            target = -1*nums[i]
            while left<right:
                sum = nums[left]+nums[right]
                if sum==target:
                    res.append([nums[i],nums[left],nums[right]])
                    right-=1
                    left+=1
                
                    while left<right and nums[left]==nums[left-1]:
                        left+=1

                    while left<right and nums[right]==nums[right+1]:
                        right-=1
                
                elif sum>target:
                    right-=1
                elif sum<target:
                    left+=1
            i+=1
        return res