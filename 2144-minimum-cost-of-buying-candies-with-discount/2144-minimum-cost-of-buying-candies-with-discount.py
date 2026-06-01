class Solution(object):
    def minimumCost(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """

        
        if len(cost)<3:
            return sum(cost)
        cost.sort(reverse=True)
        return sum(cost)-sum(cost[2::3])
