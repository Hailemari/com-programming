class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        initial_capacity = capacity
        n = len(plants)
        total_steps = 0

        for i in range(n):
            if plants[i] <= capacity:
                total_steps += 1
                capacity -= plants[i]
            
            else:
                total_steps += 2*i + 1
                capacity = initial_capacity - plants[i]



        return total_steps
        