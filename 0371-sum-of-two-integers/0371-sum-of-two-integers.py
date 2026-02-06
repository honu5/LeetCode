class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
    
        ans=[0]*2000
        print(len(ans))
        if a<0:
            for i in range(abs(a)):
                ans.pop()
        else:
            for i in range(a):
                ans.append(0)
        print(len(ans))
        if b<0:
            for i in range(abs(b)):
                ans.pop()
        else:
            for i in range(b):
                ans.append(0)
        print(len(ans))
        return len(ans)-2000
        
        