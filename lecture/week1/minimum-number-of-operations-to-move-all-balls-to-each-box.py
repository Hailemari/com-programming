class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        result = []
        
        for idx in range(n):
            step = 0
            for i in range(idx+1, n):
                if boxes[i] == "1":
                    step += i - idx
                
            for j in range(idx, -1, -1):
                if boxes[j] == "1":
                    step += idx - j
            
            result.append(step)

        return result
