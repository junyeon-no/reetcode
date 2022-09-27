from typing import List
import sys

#시간 초과(정렬)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p_s = sorted(prices)
        rst = 0
        for i,p in enumerate(prices):
            if i == len(prices) - 1 : break
            p_s.pop(p_s.index(p))
            if i == 0 : rst = p_s[-1] - p
            elif p_s[-1] - p > rst : 
                rst = p_s[-1] - p
        if rst < 0 : 
            rst = 0
        return rst

# O(n) 해결
class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        max_r = 0
        min_price = sys.maxsize
        m = float('-inf')
        m2 = float('inf')
        print( "값",m > 0,  m < 0)
        print(min_price,m, m2)
        return 0
        # for p in prices:
        #     min_price = min(p , min_price)
        #     max_r  = max(max_r, p - min_price)
        # return max_r
            


prices = [7,1,5,3,6,4]
s = Solution2()
print(s.maxProfit(prices))