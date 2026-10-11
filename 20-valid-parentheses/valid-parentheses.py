class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {'(':')','{':'}','[':']'}
        for char in s:
            if char in list(pairs):
                stack.append(char)
            else:
                if len(stack)==0:
                    return False
                if pairs[stack[-1]] != char:
                    return False
                stack.pop()
        return True if not stack else False