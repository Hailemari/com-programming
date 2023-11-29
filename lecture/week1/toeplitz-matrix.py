class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        is_toeplitz = True

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] != matrix[i - 1][j - 1]:
                    is_toeplitz = False

        
        return is_toeplitz


        