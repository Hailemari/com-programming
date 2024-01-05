class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # Use counting sort instead of the built-in sort()
        count = [0] * (limit + 1)
        for p in people:
            count[p] += 1

        i = 0
        for val in range(1, limit + 1):
            while count[val] > 0:
                people[i] = val
                i += 1
                count[val] -= 1
        
        l, r = 0, len(people) - 1
        boats = 0
        while l <= r:
            if people[l] + people[r] <= limit:
                l += 1
            r -= 1
            boats += 1

        return boats