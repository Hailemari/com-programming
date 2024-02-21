class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        arr = [1]*(rowIndex + 1)
        def pascal(rowIndex):
            if rowIndex == 1:
                return [1, 1]
            prev = pascal(rowIndex-1)
            for i in range(rowIndex, 0, -1):
                if i == 0 or i == rowIndex:
                    arr[i] = 1
                else:
                    arr[i] = prev[i - 1] + prev[i]
            
            return arr

        return pascal(rowIndex)
        
        


