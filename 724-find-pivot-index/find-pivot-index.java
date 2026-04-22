class Solution {
    public int pivotIndex(int[] nums) {
        int left = 0, right = 0, sum = 0;
        for(int element : nums){
            sum += element;
        }
        if(left == sum-left-nums[0]) return 0;
        for(int i=1; i<nums.length; i++){
            left += nums[i-1];
            right = sum - left - nums[i];
            if(left == right) return i;
        }
        return -1;
    }
}