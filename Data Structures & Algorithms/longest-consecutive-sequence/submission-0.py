class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest = 0

        for n in nums:
            if n - 1 not in numset:             # this is the starting point 
                current = n

                while current + 1 in numset:    # is next num in set?
                    current = current + 1       # then add next as current 
                
                length = current - n + 1        # length will be "4 - 1 + 1"
                longest = max(longest, length)  # keep whichever is longest yet

        return longest

                