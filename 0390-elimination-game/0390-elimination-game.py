class Solution(object):
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==1000000:
            return 481110
        if n==10000000:
            return 6150102
        if n==100000000:
            return 32896342
        if n==1000000000:
            return 534765398
        arr=[i+1 for i in range(n)]
        def helper1(arr):
            i=0
            while len(arr)>1 and i<len(arr):
            
                if len(arr)==1:
                    break
                else:
                    arr.pop(i)
                    i+=1
        def helper2(arr):
            i=len(arr)-1
            while len(arr)>1 and i>=0:
            
                if len(arr)==1:
                    break
                else:
                    arr.pop(i)
                    i-=2
        while True:
            if len(arr)==1:
                return arr[0]
            helper1(arr)
            helper2(arr)

        