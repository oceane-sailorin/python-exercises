# You are given an array prices where prices[i] is the price of a given stock on the ith day.

#You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

class Solution:
    def maxProfit(self, prices) -> int:
        max_profit = 0
        current_max = 0
        for price in reversed(prices):
            current_max = max(current_max,price)
            max_profit = max((current_max - price), max_profit)

        return max_profit


s1 = Solution()

print(s1.maxProfit([7,1,5,3,6,4]))

print(s1.maxProfit([7,6,4,3,1]))

print(s1.maxProfit([7,8,8,8,6,4]))

print(s1.maxProfit([587,125,369,541,369,542,36774,521,254]))

print(s1.maxProfit([9,0,2,3,7,8,4,2,6,8,5,0,3,6,5,2,5,6,3,7,5,6,9,8,5,3,6,2,6,5,6,3,2,5,4,1,4,5,2,3,6,4]))

print(s1.maxProfit([8754225,112365,225412,96335,8745236,854123,695669,8524,235365,225836,548822]))