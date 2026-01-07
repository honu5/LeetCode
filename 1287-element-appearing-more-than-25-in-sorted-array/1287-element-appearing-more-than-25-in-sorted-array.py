class Solution(object):
    def findSpecialInteger(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        count=Counter(arr)
        most=count.most_common()
        return most[0][0]
        