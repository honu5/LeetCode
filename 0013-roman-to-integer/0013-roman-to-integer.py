class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        val=0
        
        roman={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        if len(s)==1:
            return roman[s[0]]
        i=0
        while i<len(s)-1:
            if roman[s[i]]>=roman[s[i+1]]:
                val+=roman[s[i]]
            else:
                val+=(roman[s[i+1]]-roman[s[i]])
                i+=1
            i+=1
        if roman[s[-2]]>=roman[s[-1]]:
            val+=roman[s[-1]]
        
        return val





        