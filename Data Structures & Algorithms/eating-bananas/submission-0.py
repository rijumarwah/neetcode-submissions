import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1            # 1 hour minimum rate to eat a pile
        right = max(piles)  # Worst Case Example: 11 bananas/hour rate 
                            # to eat a pile, but we need the minimum.

        while left <= right:
            mid = (left + right) // 2

            # Calculate Total Hours
            total_hours = 0
            for pile in piles:
                total_hours += math.ceil(pile/mid)
            
            # If this is true, we already have fast enough sol, look for more
            if total_hours <= h:
                right = mid - 1
            else:
                left = mid + 1
        
        return left
