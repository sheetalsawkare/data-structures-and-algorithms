import java.util.*;
class Solution {
    public int maxSubArray(int[] nums) {
       int best = nums[0];
       int result = nums[0];
       for(int i=1; i<nums.length; i++){
            int v1 = best + nums[i];
            int v2 = nums[i];
            best = Math.max(v1, v2);
            result = Math.max(result, best);
       }
       return result;
    }
}