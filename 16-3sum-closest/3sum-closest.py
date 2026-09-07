class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        i=0
        n=len(nums)
        max_diff = float('inf')
        closest_sum = 0
        while i<n-2:
            left = i+1
            right = n-1
            while left<right:
                sum = nums[i] + nums[left] + nums[right]
                diff = abs(sum-target)
                if max_diff>diff:
                    max_diff=diff
                    closest_sum = sum
                if sum==target:
                    return sum
                elif sum<target:
                    left+=1
                else:
                    right-=1
            i+=1
        return closest_sum