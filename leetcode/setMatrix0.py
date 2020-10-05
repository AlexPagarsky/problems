class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        cols = []
        for i in range(len(matrix)):
            flag = j in cols
            for j in range(len(matrix[i])):
                if j in cols:
                    matrix[i][j] = 0
                if matrix[i][j] == 0:
                    cols.append(j)




        """
        Do not return anything, modify matrix in-place instead.
        """
        



# Input: 
# [
#   [1,1,1],
#   [1,0,1],
#   [1,1,1]
# ]
# Output: 
# [
#   [1,0,1],
#   [0,0,0],
#   [1,0,1]
# ]