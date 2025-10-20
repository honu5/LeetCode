class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """

        count=0
        for i in operations:
            if i == "X++" or i=="++X":
                count+=1
            else:
                count-=1
        return count
        