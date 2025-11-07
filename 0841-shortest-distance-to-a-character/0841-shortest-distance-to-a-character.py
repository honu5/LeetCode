class Solution(object):
    def shortestToChar(self, s, c):
        """
        :type s: str
        :type c: str
        :rtype: List[int]
        """
        a=0
        l=0
        t=-1*len(s)
        for i in range(len(s)):
            if s[i]==c:
                l=i
                break
        ans=[]
        while a<len(s):
            ans.append(min(abs(l-a),abs(a-t)))
            if a==l:
                for i in range(a+1,len(s)):
                    if s[i]==c:
                        l=i
                        t=a
                        break
            a+=1
        return ans

        