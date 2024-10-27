class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        count = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 1:
                    count += self.countMinSquares(matrix,i, j)
                    
        return count

    def countMinSquares(self, matrix, i, j):
        count = 0
        start_i = i
        start_j = j
        while i < len(matrix) and j < len(matrix[0]):
            num = i - start_i + j - start_j + 1
            for k in range(start_i, i + 1):
                if matrix[k][j] != 1:
                    return count
            for k in range(start_j, j + 1):
                if matrix[i][k] != 1:
                    return count
            count += 1
            i += 1
            j += 1
        return count

    