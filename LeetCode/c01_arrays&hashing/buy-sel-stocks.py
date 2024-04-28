"""You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. 
However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve."""

from icecream import ic

# 1. You can't sell if you haven't bought

def maxProfit(prices: list[int]) -> int:
    # profit = 0
    # buy = 0
    # sell = 0
    #
    # for i in range(1, len(prices)):  # max index = 5
    #     if prices[i - 1] < prices[i] and i != len(prices) - 1:  # buy == lower price and haven't bought
    #         if buy == 0:
    #             buy = prices[i - 1]
    #             ic(buy)
    #     elif buy > 0:  # sell
    #         sell = max(prices[i - 1], prices[i])
    #         ic(sell)
    #
    #     if sell > 0 and buy > 0:
    #         profit += sell - buy
    #         buy = 0
    #         sell = 0
    #         ic(profit)
    #     print("-----------------------")
    #
    # return 0 if profit < 0 else profit
    totalProfit = 0
    for i in range(0, len(prices) - 1):
        if (prices[i] < prices[i + 1]):
            totalProfit += prices[i + 1] - prices[i]
    return totalProfit

p1 = [7, 1, 5, 3, 6, 4]  # 7
p2 = [1, 2, 3, 4, 5]  # 4
p3 = [7, 6, 4, 3, 1]  # 0
p4 = [1,2]

print(maxProfit(p1))
print(maxProfit(p2))
print(maxProfit(p3))
print(maxProfit(p4))
