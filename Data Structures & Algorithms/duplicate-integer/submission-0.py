class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # [1,1,1,3,3,4,3,2,4,2]
        hashset = set()

        for i in nums:
            if i in hashset:
                return True
            else:
                hashset.add(i)
        return False