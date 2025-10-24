class Solution(object):
    def buyChoco(self, prices, money):
        """
        :type prices: List[int]
        :type money: int
        :rtype: int
        """
        prices.sort()
        if sum(prices[0:2])>money:
            return money
        else:
            return money-sum(prices[0:2])
        