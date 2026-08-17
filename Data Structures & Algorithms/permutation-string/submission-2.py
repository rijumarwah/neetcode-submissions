class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Edge Case
        if len(s1) > len(s2):
            return False

        count_s1 = {}
        l = 0
        r = len(s1) - 1

        for i in s1:
            count_s1[i] = 1 + count_s1.get(i, 0)

        # Build count only for first window only, edit this as we go
        count_sub = {}
        for j in range(len(s1)):
            count_sub[s2[j]] = 1 + count_sub.get(s2[j], 0)

        # This is optimal, we don't recount the substring everytime
        while r < len(s2):
            if count_sub == count_s1:
                return True
            
            # Remove the left character, and remove completely if count is 0
            count_sub[s2[l]] -= 1
            if count_sub[s2[l]] == 0:
                del count_sub[s2[l]]

            # Move both pointers 
            l += 1
            r += 1

            # Add the new right character if pointer can be moved
            if r < len(s2):
                count_sub[s2[r]] = 1 + count_sub.get(s2[r], 0)

        return False