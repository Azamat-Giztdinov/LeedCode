class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        result = 0
        seen = set()
        size = len(s)
        def backtrack(idx, curr):
            nonlocal result
            if idx == size:
                if curr and (curr not in seen):
                    result = max(len(seen) + 1, result)
                return
            curr += s[idx]
            if curr not in seen:
                seen.add(curr)
                backtrack(idx + 1, '')
                seen.remove(curr)
            backtrack(idx + 1, curr)
        backtrack(0, '')
        return result