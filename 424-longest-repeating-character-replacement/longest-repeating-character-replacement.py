class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        high=0
        low=0
        n=len(s)
        freq={}
        result = float("-inf")
        while(high<n):
            if s[high] in freq:
                freq[s[high]] = freq[s[high]] + 1
            else: 
                freq[s[high]] = 1
            
            window = high - low + 1
            max_freq = max(freq.values())
            max_replacement = window - max_freq

            if max_replacement <= k:
                valid_window = high-low+1
                result = max(result, valid_window)
            else:
                freq[s[low]] = freq[s[low]] - 1
                low+=1
            high+=1
        return result