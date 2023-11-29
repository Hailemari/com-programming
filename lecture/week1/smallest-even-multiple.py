class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if n <= 2:
            return 2
            
        if not n % 2:
            return n

        return 2 * n
        
        
        