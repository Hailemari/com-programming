class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        basket = {}
        max_fruits = 0
        curr_fruits = 0
        left = 0

        for right in range(len(fruits)):
            basket[fruits[right]] = basket.get(fruits[right], 0) + 1
            curr_fruits += 1

            while len(basket) > 2:
                basket[fruits[left]] -= 1
                if basket[fruits[left]] == 0:
                    del basket[fruits[left]]
                left += 1
                curr_fruits -= 1

            max_fruits = max(max_fruits, curr_fruits)

        return max_fruits
       
        