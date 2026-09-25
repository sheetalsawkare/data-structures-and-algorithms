class Solution:
    def get_next(self,num):
        result=0
        while num>0:
            digit = num%10
            result+=digit*digit
            num=num//10
        return result

    def isHappy(self, n: int) -> bool:

        slow=n
        fast=n
        while True:
            slow=self.get_next(slow)
            fast=self.get_next(self.get_next(fast))
            if slow==fast:
                break
        return slow==1
