class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell =100000000,0
        for i in prices:
            if i < buy:
                buy = i
            profit = i - buy
            print(profit)
            sell = max(sell , profit)
        return sell
