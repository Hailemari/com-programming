class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        n = len(tickets)
        ans = 0
        
        for i in range(n):
            if i == k:
                ans += tickets[i]
            else:
                if i < k and tickets[i] <= tickets[k]:
                    ans += tickets[i]
                if i < k and tickets[i] > tickets[k]:
                    ans += tickets[k]

                if i > k and tickets[i] < tickets[k]:
                    ans += tickets[i]
                if i > k and tickets[i] >= tickets[k]:
                    ans += tickets[k] - 1

        return ans

