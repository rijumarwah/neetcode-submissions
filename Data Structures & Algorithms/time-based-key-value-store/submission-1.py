class TimeMap:

    def __init__(self):
        self.hmap = defaultdict(list)
        # key -> [(timestamp, value), (timestamp, value), ...]

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hmap[key].append((timestamp, value))
        # {"alice": [(1, "happy"), (3, "sad"), (5, "angry")], ...}

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hmap:
            return ""

        arr = self.hmap[key]
        res = ""
        left = 0
        right = len(arr) - 1

        while left <= right:
            mid = (left + right) // 2

            if arr[mid][0] <= timestamp:
                # possible solution
                res = arr[mid][1]

                # perhaps there are better solutions, we'll keep this 
                # as best so far.
                left = mid + 1
            
            else:
                # timestamp is too large
                right = mid - 1
        
        return res
 





        
