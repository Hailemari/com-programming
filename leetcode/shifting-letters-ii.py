class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        s_order = list(map(ord, list(s)))

        pre_sum = [0] * (n + 1)

        for start, end, direction in shifts:
            if direction:
                pre_sum[start] += 1
                pre_sum[end + 1] -= 1
            else:
                pre_sum[start] += -1
                pre_sum[end + 1] -= -1
        
        for i in range(1, n):
            pre_sum[i] +=  pre_sum[i - 1]
        
        for i, order in enumerate(s_order):
            order += pre_sum[i]
            s_order[i] = chr((order - 97) % 26 + 97)
        
        return "".join(s_order)