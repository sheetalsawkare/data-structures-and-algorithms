class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        low=0
        high=k-1
        result = float('-inf')
        sum=0
        n=len(nums)

        for i in range(k):
            sum = sum+nums[i]
        
        avg = sum/k

        while high<n:
            result = max(result, avg)
            low+=1
            high+=1
            sum = sum - nums[low-1]
            if high == n:
                break
            sum = sum + nums[high]
            avg = sum/k

        return result