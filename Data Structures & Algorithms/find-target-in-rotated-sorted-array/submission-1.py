class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            
            # Left half is sorted
            if nums[left] <= nums[mid]:
                # Target is exists here
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                # Target does not exist here
                else:
                    left = mid + 1
            
            # Right half is sorted
            else: 
                # Target exists here
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                # Target does not exist here
                else:
                    right = mid - 1

        return -1