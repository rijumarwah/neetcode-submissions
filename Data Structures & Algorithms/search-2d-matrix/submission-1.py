class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in matrix:
            if i[-1] == target:
                return True
            elif i[-1] > target:
                left = 0
                right = len(i) - 1

                while left <= right:
                    mid = (left + right) // 2
                    if i[mid] == target:
                        return True
                    elif i[mid] < target:
                        left = mid + 1
                    else:
                        right = mid - 1
            else:
                continue

        return False
