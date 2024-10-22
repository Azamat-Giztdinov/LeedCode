class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        C = [0] * n
        for i in range(n):
            C[i] = len(set(A[:i + 1]) & set(B[:i + 1]))
        return C
