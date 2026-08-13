class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        longest = 0
        hset = set()
        
        for right in range(len(s)):
            while s[right] in hset:
                hset.remove(s[left])
                left += 1
            hset.add(s[right])
            longest = max(longest, right-left+1)

        return longest
            
