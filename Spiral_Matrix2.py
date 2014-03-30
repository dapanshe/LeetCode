## keep a record of the direction for insertion
## - - 1 - -
## |       |
## 4       2
## |       |
## - - 3 - -
class Solution:
    # @return a list of lists of integer
    def generateMatrix(self, n):
        i = 0
        j = 0
        matrix = []
        while i < n:
            row = []
            j = 0
            while j < n:
                row.append(0)
                j += 1
            matrix.append(row)
            i += 1
        direction = 1
        num = 1
        i = 0
        j = 0
        while num <= n*n:
            if direction == 1:
                if j < n and matrix[i][j] == 0:
                    matrix[i][j] = num
                    j += 1
                    num += 1
                else:
                    direction = 2
                    j -= 1
                    i += 1
            elif direction == 2:
                if i < n and matrix[i][j] == 0:
                    matrix[i][j] = num
                    i += 1
                    num += 1
                else:
                    direction = 3
                    i -= 1
                    j -= 1
            elif direction == 3:
                if j>=0 and matrix[i][j] == 0:
                    matrix[i][j] = num
                    j -= 1
                    num += 1
                else:
                    direction = 4
                    j += 1
                    i -= 1
            else:
                if i>=0 and matrix[i][j] == 0:
                    matrix[i][j] = num
                    i -= 1
                    num += 1
                else:
                    direction = 1
                    i += 1
                    j += 1
        return matrix
