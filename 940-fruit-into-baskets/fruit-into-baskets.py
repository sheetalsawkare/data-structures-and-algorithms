class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        high=0
        low=0
        res=float("-inf")
        freq={}
        n=len(fruits)
        while(high<n):
            if fruits[high] in freq:
                freq[fruits[high]] = freq[fruits[high]] + 1
            else:
                freq[fruits[high]] = 1

            while len(freq) > 2:
                freq[fruits[low]] = freq[fruits[low]] - 1
                if freq[fruits[low]] == 0:
                    del freq[fruits[low]]
                
                low+=1
            
            window = high - low + 1
            res = max(res, window)

            high+=1
        return res