class Solution:
    def maxArea(self, heights: List[int]) -> int:
        highest_vol = 0

        left = 0
        right = len(heights) - 1

        while left < right:
            vol = min(heights[left], heights[right]) * (right-left)
            if vol > highest_vol:
                highest_vol = vol

            # We move the bars based on which bar is shorted ->
            # if bar is shorter, move it
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return highest_vol