class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hmap = {}

        for i in range(0, len(nums)):
            search = target - nums[i]
            if search in hmap:
                return [hmap[search], i]
            else:
                hmap[nums[i]] = i
        