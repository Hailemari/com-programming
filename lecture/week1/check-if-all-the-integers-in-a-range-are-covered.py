class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        n = len(ranges)
        found = False

        for i in range(left, right + 1):
            for j in range(n):
                if i >= ranges[j][0] and i <= ranges[j][1]:
                    found = True
                    break
                found = False
            
            if not found:
              return False
        
        if found:
          return True
        else:
          return False



            
