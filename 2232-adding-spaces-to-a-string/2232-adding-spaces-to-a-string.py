class Solution(object):
    def addSpaces(self, s, spaces):
        """
        :type s: str
        :type spaces: List[int]
        :rtype: str
        """
        '''s=list(s)
        n=0
        for i in spaces:
            s.insert(i+n," ")
            n+=1
        return "".join(s)'''
        '''n=0
        for i in spaces:
            s=s[:i+n]+" "+s[i+n:]
            n+=1
        return s'''
        j=0
        res=[]
        for i in range(len(s)):
            if j<len(spaces) and i==spaces[j]:
                res.append(" ")
                j+=1
            res.append(s[i])
        return "".join(res)

        