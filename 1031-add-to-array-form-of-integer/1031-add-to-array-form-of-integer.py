class Solution(object):
    def addToArrayForm(self, num, k):
        """
        :type num: List[int]
        :type k: int
        :rtype: List[int]
        """
    
        string=[str(x) for x in num]
        ans="".join(string)
        ans=int(ans)+k
        ans=str(ans)
        hello=[]
        for i in ans:
            hello.append(int(i))
        return hello
        