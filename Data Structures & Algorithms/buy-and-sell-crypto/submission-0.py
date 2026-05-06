class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minn = float('inf')
        maxp = 0
        for i in prices:
            if i<minn:
                minn=i
            elif i-minn>maxp:
                maxp=i-minn
        return maxp