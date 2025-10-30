class Solution(object):
    def minOperations(self, logs):
        """
        :type logs: List[str]
        :rtype: int
        """
        count=0
        for i in logs:
            if i=="../":
                count=max(0,count-1)
            elif i!="./":
                count+=1
        return count
        