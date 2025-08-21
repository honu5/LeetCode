class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dic={")":"("
        ,"]":"[",
        "}":"{"}

        arr=[]

        for i in s:
            if i in dic:
                if not arr:
                    return False
                popped=arr.pop()
                if popped!=dic[i]:
                    return False
            else:
                arr.append(i)
        if arr:
            return False
        return True
        