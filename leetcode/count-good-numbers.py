class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7
        
        # Calculate number of odd and even positions
        odd_positions = n // 2
        even_positions = n // 2 + n % 2
        
        # Calculate total count using binary exponentiation
        total_count = (self.binaryExp(5, even_positions) * self.binaryExp(4, odd_positions)) % MOD
        return total_count
    
    def binaryExp(self, x, n):
        MOD = 10**9 + 7
        
        # Base case
        if n == 0:
            return 1

        # Handle negative exponents
        if n < 0:
            return 1 / self.binaryExp(x, -n)
        
        # Recursive binary exponentiation
        if n % 2 == 0:
            return self.binaryExp((x*x) % MOD, n // 2)
        else:
            return x * self.binaryExp((x*x) % MOD, (n-1) // 2)
