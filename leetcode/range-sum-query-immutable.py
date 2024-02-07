class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        accumulator = 0
        n = len(self.nums)
        for i in range(n):
            self.nums[i] += accumulator
            accumulator = self.nums[i]

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.nums[right]
        else:
            return self.nums[right] - self.nums[left - 1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)