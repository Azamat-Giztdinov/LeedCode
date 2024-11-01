class Solution:
    def makeFancyString(self, s: str) -> str:
        count = 1
        rest_s = s[0]

        for i in range(1, len(s)):
            if s[i] != rest_s[-1]:
                count = 1
                rest_s += s[i]
            elif count < 2:
                count+=1
                rest_s += s[i]
        return rest_s