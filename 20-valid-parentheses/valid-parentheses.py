class Solution:
    def isValid(self, s: str) -> bool:
        ch = []
        par = {']': '[', ')': '(', '}': '{'}
        for i in s:
            if i in '[{(':
                ch.append(i)
            elif ch and ch[-1] == par[i]:
                ch.pop()
            else:
                return False
        return not ch