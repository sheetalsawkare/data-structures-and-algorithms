import java.util.*;
class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        int l=0, result = Integer.MAX_VALUE;
        int sum = 0;
        for(int h=0; h<nums.length; h++){
            sum += nums[h]; 
            
            while(sum >= target){
               int len = h-l+1;
               result = Math.min(len, result);
               sum -= nums[l];
               l++;
            }
        }
        if(result == Integer.MAX_VALUE){
            return 0;
        }
        else{
            return result;
        }
    }
}