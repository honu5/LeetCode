class Solution(object):
    def fillCups(self, amount):
        """
        :type amount: List[int]
        :rtype: int
        """
        amount.sort(reverse=True)
        first=amount[0]
        total=sum(amount)
        return max(first,(total+1)//2)