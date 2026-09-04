class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        unique_idx = 0
        for i in nums:
            if i==val:
                continue
            else:
                nums[unique_idx] = i
                unique_idx+=1
        return unique_idx