class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = []
        for i in s:
            if i.isalnum() and i != " ":
                clean.append(i.lower())

        left = 0
        right = len(clean) - 1

        while left < right:
            if clean[left] == clean[right]:
                left += 1
                right -= 1
            elif clean[left] != clean[right]:
                return False

        return True