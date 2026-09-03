class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique,low,high=1,0,1
        while(high<len(nums)):
            if nums[high] != nums[high-1]:
                nums[low+1]=nums[high]
                low+=1
                unique+=1
            high+=1
        return unique