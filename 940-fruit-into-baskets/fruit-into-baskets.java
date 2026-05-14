import java.util.*;
class Solution {
    public int totalFruit(int[] fruits) {
        int low=0, result=Integer.MIN_VALUE;
        HashMap<Integer, Integer> hashmap = new HashMap<>();
        for(int high=0; high<fruits.length; high++)
        {
            hashmap.put(fruits[high], hashmap.getOrDefault(fruits[high], 0) + 1);

            while(hashmap.size() > 2){
                hashmap.put(fruits[low], hashmap.get(fruits[low]) - 1);
                if(hashmap.get(fruits[low]) == 0){
                    hashmap.remove(fruits[low]);
                }
                low++;
            }
            int length = high - low + 1;
            result = Math.max(result, length);
        }
        return result;
    }
}