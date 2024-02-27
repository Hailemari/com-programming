class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True

        if nums[0] == 0:
            return False       

        zeros = []
        for i, num in enumerate(nums):
            if num == 0:
                zeros.append(i)
        
        if not len(zeros):
            return True

        if len(zeros) == 1 and zeros[0] == n - 1:
            return True

        print(zeros)
        flag = []
        for idx in zeros:
            for j in range(idx):
                if nums[j] > idx - j:
                    flag.append(True)
                    break
                if idx == n - 1 and nums[j] == idx - j:
                    flag.append(True)
                    break

        return len(flag) == len(zeros)
