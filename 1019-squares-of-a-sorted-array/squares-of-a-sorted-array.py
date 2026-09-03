class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        pos = []
        neg = []
        res = []

        for i in nums:
            if i>=0:
                pos.append(i)
            else:
                neg.append(i)

        pos = [x * x for x in pos] #square
        neg = [x * x for x in neg][::-1] #square and reverse
        n,m = len(pos), len(neg)

        i,j=0,0
        while(i<n and j<m):
            if pos[i] < neg[j]:
                res.append(pos[i])
                i+=1
            else:
                res.append(neg[j])
                j+=1

        while(i<len(pos)):
            res.append(pos[i])
            i+=1

        while(j<len(neg)):
            res.append(neg[j])
            j+=1

        return res