class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1      # mid + 1, as mid cannot be minimum
            elif nums[mid] < nums[right]:
                right = mid         # mid, as mid can itself also be minimum

            
        return nums[left]           # at the end, right and left are the same element