class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def helper(base, exponent):
            if exponent == 0:
                return 1
            elif exponent % 2 == 0:
                res = helper(base, exponent // 2)
                return res * res
            else:
                res = helper(base, exponent // 2)
                return base*res*res

        ans = helper(x, abs(n))

        return float(ans) if n >= 0 else 1 / float(ans)

        
    