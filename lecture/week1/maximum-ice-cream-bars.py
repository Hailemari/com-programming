class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        max_cost = max(costs)

        count = [0]*(max_cost + 1)
        for cost in costs:
            count[cost] += 1

        sorted_costs = []
        for i in range(len(count)):
            sorted_costs.extend([i]*count[i])
        
        ans = 0
        for cost in sorted_costs:
            coins -= cost
            if coins >= 0:
                ans += 1
            else:
                break

        return ans