class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count_s = {}
        count_t = {}

        for num_s in s:
            count_s[num_s] = 1 + count_s.get(num_s, 0)
        for num_t in t:
            count_t[num_t] = 1 + count_t.get(num_t, 0)

        for i in count_s:
            if count_s[i] != count_t.get(i, 0):
                return False

        return True