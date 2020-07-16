#When to Buy and sell stock leetcode 121
class StockSolution:
    def maxProfit(self, prices):
        if len(prices) == 0:
            return 0
        minPrice = prices[0]
        maxProfit = 0
        for i in range(len(prices)):
            if prices[i] < minPrice:
                minPrice = prices[i]
            elif prices[i] - minPrice > maxProfit:
                maxProfit = prices[i] - minPrice
        return maxProfit

#When to buy and sell stock with multiple transactions leetcode 122
class Stock2Solution:
    def maxProfit(self, prices):
        if len(prices) == 0:
            return 0
        profit = 0
        for i in range(len(prices) - 1):
            if prices[i + 1] > prices[i]:
                profit += prices[i + 1] - prices[i]
        return profit

#checks if a sentence is a palidrome leetcode 125
class SentencePalindromeSolution:
    def isPalindrome(self, s):
        if s == "":
            return True
        palinS = [char.lower() for char in s if char.isalnum()]
        return palinS == palinS[::-1]
