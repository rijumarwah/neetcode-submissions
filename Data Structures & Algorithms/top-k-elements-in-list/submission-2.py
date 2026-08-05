class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # nums = [1,2,2,3,3,3], k = 2
        hmap = {}
        for i in nums:
            hmap[i] = 1 + hmap.get(i, 0)

        sorted_hmap = {k: v for k, v in sorted(hmap.items(), key = lambda item : item[1], reverse=True)} # .items() turns it into tuple (k,v), item[1] keeps just the v, and reverses based on it

        output = []
        for j in sorted_hmap:
            output.append(j)
        
        return output[:k]