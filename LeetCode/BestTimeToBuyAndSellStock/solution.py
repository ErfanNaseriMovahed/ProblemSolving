class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return(0)
        sellIndex = 1
        buy = prices[0]
        maxProf = prices[1] - prices[0]
        for i in range(len(prices)-1):
            sell = prices[sellIndex]
            if prices[i] < buy:
                buy = prices[i]
            profit = sell - buy
            sellIndex += 1
            maxProf = max(maxProf, profit)
        if maxProf > 0:
            return(maxProf)
        else:
            return(0)

'''
eat pressure...
'''