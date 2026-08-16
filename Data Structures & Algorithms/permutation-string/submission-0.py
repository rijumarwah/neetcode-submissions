class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count_s1 = {}
        l = 0
        r = len(s1) - 1

        for i in s1:
            count_s1[i] = 1 + count_s1.get(i, 0)

        while r < len(s2):
            sub = s2[l : r + 1]
            count_sub = {}
            for j in sub:
                count_sub[j] = 1 + count_sub.get(j, 0)

            if count_sub == count_s1:
                return True

            l += 1
            r += 1

        return False