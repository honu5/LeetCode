class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        if str(x)[-1]==0:
            val= int(str(x)[-2::-1])
        if str(x)[0]=="-":
            val = -1*int(str(x)[-1:0:-1])
        else:
            val = int(str(x)[::-1])
        if val>=(2**31)-1 or val<=((-2)**31):
            return 0
        return val


        