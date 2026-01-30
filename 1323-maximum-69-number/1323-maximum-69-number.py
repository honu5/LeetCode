class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        lst=list(str(num))
        for i in range(len(lst)):
            if lst[i]=="6":
                lst[i]="9"
                break
        print(lst)
        return int("".join(lst))
        