class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        count=Counter(arr)
        most=count.most_common()
        x=[i[1] for i in most ]
        if len(x)!=len(set(x)):
            return False
        return True
        