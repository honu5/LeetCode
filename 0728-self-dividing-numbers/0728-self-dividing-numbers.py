class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        ans=[]
        for i in range(left,right+1):
            if len(str(i))==1:
                ans.append(i)
            elif '0' in str(i):
                continue
            else:
                Found=True 
                for j in str(i):
                    if i%int(j)!=0:
                        Found=False
                        break
                if Found:
                    ans.append(i)
        return ans

        