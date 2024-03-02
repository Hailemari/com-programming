class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        water = 0

        for i, h in enumerate(height):
            while stack and height[stack[-1]] < h:
                peak = stack.pop()

                if not stack:
                    break

                width = i - stack[-1] - 1
                water_height = min(height[i], height[stack[-1]]) - height[peak]
                water += width * water_height

            
            stack.append(i)

        return water