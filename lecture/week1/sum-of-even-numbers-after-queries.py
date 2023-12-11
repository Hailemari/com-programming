class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        ans = []
        even_nums = [num for num in nums if num % 2 == 0]
        even_sum = sum(even_nums)

        for val, idx in queries:
            even_before = True
            if nums[idx] % 2:
                even_before = False

            curr = nums[idx]
            nums[idx] += val

            if nums[idx] % 2 == 0 and not even_before:
                even_sum += nums[idx]
            elif nums[idx] % 2 == 0 and even_before:
                even_sum += val
            elif nums[idx] % 2 != 0 and even_before:
                even_sum -= curr

            ans.append(even_sum)
            
       
        return ans