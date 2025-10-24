class Solution(object):
    def splitNum(self, num):
        """
        :type num: int
        :rtype: int
        """
        ans=list(str(num))
        ans.sort()
        
        left=''
        right=''
        m=int((len(ans)/2.0)+0.7)
        for i in range(len(ans)):
            if i%2==0:
                left+=ans[i]
            else:
                right+=ans[i]
        return int(left)+int(right)
        
        

        