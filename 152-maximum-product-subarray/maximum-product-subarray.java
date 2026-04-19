import java.util.*;
class Solution {
    public int maxProduct(int[] nums) {
       int max_best = nums[0];
       int min_best = nums[0];
       int result = nums[0];

        for(int i=1; i<nums.length; i++){
            int v1 = max_best*nums[i];
            int v2 = min_best*nums[i];
            int v3 = nums[i];
            
            max_best = Math.max(v1, Math.max(v2,v3));
            min_best = Math.min(v1, Math.min(v2,v3));
            result = Math.max(result, Math.max(max_best,min_best));
        }
        return result;
    }
}