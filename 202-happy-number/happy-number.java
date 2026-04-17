class Solution {

    public int next(int num){
        int sum = 0;
        while(num > 0){
            int digit = num%10;
            sum += digit*digit;
            num = num/10;
        }
        return sum;
    }

    public boolean isHappy(int n) {
        int slow = n;
        int fast = next(n);

        while(slow != fast){
            slow = next(slow);
            fast = next(next(fast));
        }
        if(slow == 1) return true;
        return false;
    }
}