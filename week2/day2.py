#Pascal's triangle
class PascalSolution:
    def generate(self, numRows):
        if numRows == 0:
            return []
        triangle = []
        first_row = [1]
        triangle.append(first_row)
        for i in range(1, numRows):
            prev = triangle[i - 1]
            row = []
            row.append(1)
            for j in range(1, i):
                row.append(prev[j - 1] + prev[j])
            row.append(1)
            triangle.append(row)
        return triangle

#returns row of the rowindex of pascal's triangle
class PascalRowSolution:
    def getRow(self, rowIndex):
        pascal = [1]*(rowIndex + 1)
        for i in range(2,rowIndex+1):
            for j in range(i-1,0,-1):
                pascal[j] += pascal[j-1]
        return pascal
