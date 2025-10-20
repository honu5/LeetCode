class Solution(object):
    def findLeastNumOfUniqueInts(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        if len(arr)<=k:
            return 0
        if len(arr)==1 and k==0:
            return 1
        count=Counter(arr)
        most=count.most_common()
        n=most[-1][1]
        while k:
            k-=1
            n-=1
            
            if n==0:
                most.pop()
                n=most[-1][1]
            
        return len(most)
