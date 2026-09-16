class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        k=len(p)
        p_hash = {}
        s_hash = {}
        result = []
        low=0
        high=k-1

        for char in p:
            if char in p_hash:
                p_hash[char] = p_hash[char]+1
            else:
                p_hash[char]=1

        if len(p) > len(s):
            return []
        else:
            for i in range(k):
                if s[i] in s_hash:
                    s_hash[s[i]] = s_hash[s[i]]+1
                else:
                    s_hash[s[i]]=1

            while high<len(s):
                if s_hash == p_hash:
                    result.append(low)

                low+=1
                high+=1
                
                if high == len(s):
                    break

                if s[low-1] in s_hash:
                    s_hash[s[low-1]] = s_hash[s[low-1]] - 1

                if s_hash[s[low-1]] == 0:
                    s_hash.pop(s[low-1])

                if s[high] in s_hash:
                    s_hash[s[high]] = s_hash[s[high]]+1
                else:
                    s_hash[s[high]] = 1
        return result