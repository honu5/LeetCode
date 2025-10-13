class Solution(object):
    def smallestNumber(self, num):
        """
        :type num: int
        :rtype: int
        """
        if len(str(num))==1:
            return num
        ans=[]
        for i in str(num):
            ans.append(i)

        
        if num>0:
            ans.sort()
            if int(ans[0])==0:
                for i in ans:
                    if int(i)>0:
                        idx=ans.index(i)
                        slced=ans[0:idx]
                        ans=ans[idx:]
                        print(slced)
                        break
            
                ans[1:1]=slced
                print(ans)                                
        else:
            ans.sort(reverse=True)
            ans.insert(0,'-')
            ans=ans[0:-1]
        value = ''.join(ans)
        return int(value)

       
        