class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        count = 0
        low = 0
        high = k-1
        n=len(s)
        vowel = {'a','e','i','o','u'}
        for i in range(k):
            if s[i] in vowel:
                count+=1
        result = count
        while high<n:
            high+=1
            low+=1
            if s[low-1] in vowel:
                count-=1
            if high == n:
                break
            if s[high] in vowel:
                count+=1
            result = max(result, count)
        return result