class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        size = len(A)
        present = defaultdict(int)
        C = [0] * size
        for i in range(size):
            present[A[i]] += 1
            if present[A[i]] == 2:
                C[i] += 1
            present[B[i]] += 1
            if present[B[i]] == 2:
                C[i] += 1
            C[i] += C[i - 1] if i > 0 else 0
        return C   