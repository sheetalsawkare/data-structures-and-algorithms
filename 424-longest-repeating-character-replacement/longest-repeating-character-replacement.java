import java.util.*;
class Solution {
    public static int find_max(int[] arr){
        int max = arr[0];  
    
        for(int i = 1; i < arr.length; i++){
            if(arr[i] > max){
                max = arr[i];
            }
        }
        return max;
    }

    public int characterReplacement(String s, int k) {
        int l=0, result = Integer.MIN_VALUE;
        int[] freq = new int[256];
        
        for(int h=0; h<s.length(); h++){
            char ch = s.charAt(h);
            freq[ch]++;
            
            int len = h - l + 1;
            int max_count = find_max(freq);
            int diff = len - max_count;
            
            while(diff > k){
                char low_ch = s.charAt(l);
                freq[low_ch]--;
                l++;
                
                len = h - l + 1;
                max_count = find_max(freq);
                diff = len - max_count;
            }
            
            len = h - l + 1;
            result = Math.max(len, result);
        }
        return result;
    }
}