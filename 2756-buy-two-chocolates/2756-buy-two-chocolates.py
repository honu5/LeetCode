class Solution(object):
    def buyChoco(self, prices, money):
        """
        :type prices: List[int]
        :type money: int
        :rtype: int
        """
        prices.sort()
        chck=sum(prices[0:2])
        if chck>money:
            return money
        else:
            return money-chck
        