class Solution {
    public int maxSubarraySumCircular(int[] nums) {
        int min_best = nums[0];
        int max_best = nums[0];
        int max_sum = nums[0];
        int min_sum = nums[0];
        int sum_of_arr = nums[0];

        if(nums.length == 1) return nums[0];

        for(int i=1;i<nums.length;i++){
            max_best = Math.max(max_best + nums[i],nums[i]);
            max_sum = Math.max(max_sum, max_best);

            min_best = Math.min(min_best + nums[i],nums[i]);
            min_sum = Math.min(min_sum, min_best);
            sum_of_arr += nums[i];
        }

        if(max_sum < 0) return max_sum;
        return Math.max(max_sum, sum_of_arr - min_sum);
    }
}