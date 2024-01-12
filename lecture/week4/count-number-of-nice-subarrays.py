class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def countSubarraysWithOdds(nums, max_odds):
            window_start = 0
            odds_in_window = 0
            valid_subarrays = 0

            for window_end in range(len(nums)):
                if nums[window_end] % 2:
                    odds_in_window += 1
                while odds_in_window > max_odds:
                    if nums[window_start] % 2:
                        odds_in_window -= 1
                    window_start += 1
                
                valid_subarrays += window_end - window_start + 1
            
            return valid_subarrays
        
        return countSubarraysWithOdds(nums, k) - countSubarraysWithOdds(nums, k - 1)

