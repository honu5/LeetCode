class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        if len(strs)==1:
            return strs[0]
        strs.sort(key=len)
        short=strs[0]
        
        ans=""
        val=""
        test=""
        j=0
        while j<len(short):
            test+=short[j]
            print(test)
            for i in range(1,len(strs)):            
                if not strs[i].startswith(test):
                    return test[:-1]
               

            j+=1
        return test[:len(test)]

        

        