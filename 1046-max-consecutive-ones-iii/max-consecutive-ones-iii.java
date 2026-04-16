import java.util.*;
class Solution {
    public int longestOnes(int[] nums, int k) {
        int l=0, result = Integer.MIN_VALUE;
        int zeroCount = 0;

        for(int h=0; h<nums.length; h++){
            if(nums[h] == 0){
                zeroCount++;
            }
            while(zeroCount > k){
                if(nums[l] == 0){
                    zeroCount--;
                }
               l++;
            }
            
            int len = h - l + 1;
            result = Math.max(len, result);
        }
        return result;
    }
}