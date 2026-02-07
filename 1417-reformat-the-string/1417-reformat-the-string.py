class Solution(object):
    def reformat(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s)==1:
            return s
        num=[]
        t=[]
        ans=""
        for i in s:
            if i.isdigit():
                num.append(i)
            else:
                t.append(i)
        if abs(len(num)-len(t))>1:
            return ""
        if len(num)>=len(t):
            for i in range(len(num)-1):
                ans+=num[i]
                ans+=t[i]
            if len(num)>len(t):
                ans+=num[-1]
            else:
                ans+=num[-1]
                ans+=t[-1]
        else: 
            for i in range(len(num)):
                ans+=t[i]
                ans+=num[i]
            ans+=t[-1]
        return ans
        