class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s) + 1
        cumulative_shifts = [0] * (n)
        res = []

        for start, end, direction in shifts:
            shift_direction = 1 if direction == 1 else -1
            cumulative_shifts[start] += shift_direction
            cumulative_shifts[end + 1] -= shift_direction

        for i in range(n - 1):
            if i != 0:
                cumulative_shifts[i] += cumulative_shifts[i - 1]

            new_ascii = (ord(s[i]) - ord("a") + cumulative_shifts[i]) % 26 + ord("a")
            res.append(chr(new_ascii))

        return ''.join(res)