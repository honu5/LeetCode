class Solution(object):
    def buyChoco(self, prices, money):
        """
        :type prices: List[int]
        :type money: int
        :rtype: int
        """
        prices.sort()
        chck=prices[0]+prices[1]
        if chck>money:
            return money
        else:
            return money-chck
        