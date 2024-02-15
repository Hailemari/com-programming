class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = {}

        for ans in answers:
            if ans in count:
                count[ans] += 1
            else:
                count[ans] = 1

        min_rabbits = 0
        for ans, freq in count.items():
            min_rabbits += ((freq // (ans + 1))*(ans + 1)) + (ans + 1) if freq % (ans + 1) else freq
        
        return min_rabbits
        