class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ch_set = set()
        size = 0
        left = 0
        for i in range(len(s)):
            if s[i] not in ch_set:
                ch_set.add(s[i])
                size = max(size, i - left + 1)
            else:
                while s[i] in ch_set:
                    ch_set.remove(s[left])
                    left += 1
                ch_set.add(s[i])
        return size