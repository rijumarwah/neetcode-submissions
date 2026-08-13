class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_p = 0
        left = 0
        right = 1

        while right < len(prices):
            # is profitable?
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                max_p = max(max_p, profit)
            else:
                left = right    # shift left pointer all the way to where right
                                # is as we found a very low price. 
            right += 1

        return max_p