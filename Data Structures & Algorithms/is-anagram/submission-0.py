class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # s = "racecar", t = "carrace"
        if len(s) != len(t):
            return False

        seen_s = {}
        seen_t = {}
        
        for i in s:
            if i in seen_s:
                seen_s[i] = seen_s[i] + 1
            else:
                seen_s[i] = 1

        for j in t:
            if j in seen_t:
                seen_t[j] = seen_t[j] + 1
            else:
                seen_t[j] = 1

        if seen_t == seen_s:
            return True
        else:
            return False
        