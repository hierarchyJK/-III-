class Solution1(object):
    def maxProfit(self, prices):
        """
        买卖股票的最佳时机 III
        -------------------------------------
        示例 1:

        输入: [3,3,5,0,0,3,1,4]
        输出: 6
        解释: 在第 4 天（股票价格 = 0）的时候买入，在第 6 天（股票价格 = 3）的时候卖出，这笔交易所能获得利润 = 3-0 = 3 。
        随后，在第 7 天（股票价格 = 1）的时候买入，在第 8 天 （股票价格 = 4）的时候卖出，这笔交易所能获得利润 = 4-1 = 3 。
        -------------------------------------
        示例 2:

        输入: [1,2,3,4,5]
        输出: 4
        解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
        注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。
        因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。
        -------------------------------------
        示例 3:

        输入: [7,6,4,3,1]
        输出: 0
        解释: 在这个情况下, 没有交易完成, 所以最大利润为 0
        -------------------------------------
        :type prices: List[int]
        :rtype: int
        """
        if not prices or len(prices) == 1:
            return 0

        # 用a表示从0-i之间，只做一次买卖的最大利润
        a = [0] * len(prices)
        a_min = prices[0]
        for i in range(1, len(prices)):
            a[i] = max(a[i - 1], prices[i] - a_min)
            if prices[i] < a_min:
                a_min = prices[i]

        # 用b表示从i+1~最后，只做一次买卖的最大利润，从后开始遍历
        b = [0] * len(prices)
        b_max = prices[len(prices) - 1]
        for i in reversed(range(len(prices) - 1)):
            b[i] = max(b[i + 1], b_max - prices[i])
            if prices[i] > b_max:
                b_max = prices[i]

        # 遍历一下每天，选出最大的两数之和就是最大股票收益
        res = 0
        for i in range(1, len(prices) - 1):
            temp = a[i] + b[i + 1]
            if (temp > res):
                res = temp

        return max(res, b[0])  # return max(res, a[len(a)-1]),正序排列时候


# print(Solution1().maxProfit([1,2,4,2,5,7,2,4,9,0]))
# print(Solution1().maxProfit([3,3,5,0,0,3,1,4]))
# print(Solution1().maxProfit([1,2,3,4,5]))
# print(Solution1().maxProfit([2,1,2,0,1]))
# Solution1().maxProfit([1,2,3,4,5])
# print(Solution1().maxProfit([5,4,3,2,1]))
