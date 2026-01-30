class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n%2==0:
            ans=[]
        else:
            ans=[0]
        n-=1
        l=1
        while n>0:
            ans.append(l)
            ans.insert(0,-1*l)
            n-=2
            l+=1
        return ans
        