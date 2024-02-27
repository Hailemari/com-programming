class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        
        def helper(nums, start, end, memo):
            # Base case: if there's only one element left, the current player can choose it and win
            if start == end:
                return nums[start]

            # Check if the result for the this state is already calculated
            if (start, end) in memo:
                return memo[(start, end)]

            # Player one's turn: maximize their score
            score1 = nums[start] - helper(nums, start + 1, end, memo)
            score2 = nums[end] - helper(nums, start, end - 1, memo)

            # Store the maximum score for the current state
            memo[(start, end)] = max(score1, score2)

            return memo[(start, end)]

        
        return helper(nums, 0, len(nums) - 1, {}) >= 0