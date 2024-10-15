class Solution:
    def minimumSteps(self, s: str) -> int:
        count = 0
        idx = 0
        for i, char in enumerate(s):
            if char == '0':
                count += (i - idx)
                idx += 1

        return count