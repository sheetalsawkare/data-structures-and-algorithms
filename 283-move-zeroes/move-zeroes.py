class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        unique_index=0
        for i in nums:
            if not i==0:
                nums[unique_index]=i
                unique_index+=1
            
        diff = len(nums)-unique_index

        for i in range(diff):
            nums[unique_index]=0
            unique_index+=1