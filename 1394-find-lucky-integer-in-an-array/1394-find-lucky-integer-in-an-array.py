class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        count=Counter(arr)
        ans=[]
        for frq,num in count.items():
            if frq==num:
                ans.append(frq)
        if ans:
            return max(ans)
        return -1
        