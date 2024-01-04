class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        def next_index(i):
            return (i + nums[i]) % len(nums)
    
        for i in range(len(nums)):
            if nums[i] == 0:
                continue  # This index has already been visited or marked as part of a non-loop path
            
            # Determine the direction of the movement: forward (True) or backward (False)
            direction = nums[i] > 0
            slow = i
            fast = i
            
            while True:
                # Move one step for slow pointer
                slow = next_index(slow)
                if nums[slow] == 0 or (nums[slow] > 0) != direction:
                    break  # Not a valid cycle
                
                # Move two steps for fast pointer
                fast = next_index(fast)
                if nums[fast] == 0 or (nums[fast] > 0) != direction:
                    break
                fast = next_index(fast)
                if nums[fast] == 0 or (nums[fast] > 0) != direction:
                    break
                
                if slow == fast:
                    if slow == next_index(slow):  # Single element loop
                        break
                    return True  # Cycle found
            
            # Mark the elements on the non-loop path with 0
            slow = i
            while nums[slow] != 0 and (nums[slow] > 0) == direction:
                jump = next_index(slow)
                nums[slow] = 0
                slow = jump
        
        return False