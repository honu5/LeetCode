class Solution(object):
    def isValid(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word)<3:
            return False
        vow=["A","E","I","O","U","a","e","i","o","u"]
        ans=[True,False,False]
        for i in word:
            if not i.isdigit() and not i.isalpha():
                
                return False
            if i.isalpha():
                if i in vow:
                    ans[1]=True
                else:
                    ans[2]=True
                
        print(ans)
        if False in ans:
            return False
        return True
            

    